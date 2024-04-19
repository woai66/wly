/*********************************************************************************************************************
* CH32V307VCT6 Opensourec Library 即（CH32V307VCT6 开源库）是一个基于官方 SDK 接口的第三方开源库
* Copyright (c) 2022 SEEKFREE 逐飞科技
*
* 本文件是CH32V307VCT6 开源库的一部分
*
* CH32V307VCT6 开源库 是免费软件
* 您可以根据自由软件基金会发布的 GPL（GNU General Public License，即 GNU通用公共许可证）的条款
* 即 GPL 的第3版（即 GPL3.0）或（您选择的）任何后来的版本，重新发布和/或修改它
*
* 本开源库的发布是希望它能发挥作用，但并未对其作任何的保证
* 甚至没有隐含的适销性或适合特定用途的保证
* 更多细节请参见 GPL
*
* 您应该在收到本开源库的同时收到一份 GPL 的副本
* 如果没有，请参阅<https://www.gnu.org/licenses/>
*
* 额外注明：
* 本开源库使用 GPL3.0 开源许可证协议 以上许可申明为译文版本
* 许可申明英文版在 libraries/doc 文件夹下的 GPL3_permission_statement.txt 文件中
* 许可证副本在 libraries 文件夹下 即该文件夹下的 LICENSE 文件
* 欢迎各位使用并传播本程序 但修改内容时必须保留逐飞科技的版权声明（即本声明）
*
* 文件名称          zf_device_mt9v03x
* 公司名称          成都逐飞科技有限公司
* 版本信息          查看 libraries/doc 文件夹内 version 文件 版本说明
* 开发环境          MounRiver Studio V1.8.1
* 适用平台          CH32V307VCT6
* 店铺链接          https://seekfree.taobao.com/
*
* 修改记录
* 日期                                      作者                             备注
* 2021-12-23        大W            摄像头采集完成标志位增加volatile修饰
* 2022-03-26        大W            修改部分不重要的注释
* 2022-09-15        大W            first version
********************************************************************************************************************/
/*********************************************************************************************************************
* 接线定义：
*                   ------------------------------------
*                   模块管脚            单片机管脚
*                   TXD                 查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_COF_UART_TX        宏定义
*                   RXD                 查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_COF_UART_RX        宏定义
*                   D0                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D0_PIN             宏定义
*                   D1                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D1_PIN             宏定义
*                   D2                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D2_PIN             宏定义
*                   D3                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D3_PIN             宏定义
*                   D4                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D4_PIN             宏定义
*                   D5                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D5_PIN             宏定义
*                   D6                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D6_PIN             宏定义
*                   D7                  查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_D7_PIN             宏定义
*                   PCLK                查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_PCLK_PIN           宏定义
*                   VSYNC               查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_VSY_PIN            宏定义
*                   HSYNC               查看 zf_device_mt9v03x_dvp.h 中 MT9V03X_HERF_PIN           宏定义
*                   ------------------------------------
********************************************************************************************************************/

#include "zf_driver_delay.h"
#include "zf_driver_dvp.h"
#include "zf_driver_soft_iic.h"


#include "zf_device_camera.h"
#include "zf_device_type.h"
#include "zf_device_mt9v03x_dvp.h"
#include "zf_device_config.h"

vuint8 mt9v03x_finish_flag = 0;                                                 // 一场图像采集完成标志位
__attribute__((aligned(4))) uint8 mt9v03x_image[MT9V03X_H][MT9V03X_W];

static fifo_struct          *camera_receiver_fifo;
static mt9v03x_type_enum    mt9v03x_type = MT9V03X_SCCB;
static uint16               mt9v03x_version = 0x00;

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     配置摄像头内部配置信息
// 参数说明     buff            发送配置信息的地址scc8660_sccb_set_config
// 返回参数     uint8           1-失败 0-成功
// 使用示例     mt9v03x_set_config(mt9v03x_set_confing_buffer);
// 备注信息     内部调用
//-------------------------------------------------------------------------------------------------------------------
static uint8 mt9v03x_set_config (const int16 buff[MT9V03X_CONFIG_FINISH][2])
{
    uint8   uart_buffer[4];
    uint8   return_state        = 1;
    uint16  temp_value          = 0;
    uint16  timeout_count       = 0;
    uint32  loop_count          = 0;
    uint32  uart_buffer_index   = 0;

    switch(mt9v03x_version)
    {
        case 0x0230:    loop_count = MT9V03X_PCLK_MODE;  break;
        default:        loop_count = MT9V03X_GAIN;       break;
    }
    // 设置参数  具体请参看问题锦集手册
    // 开始配置摄像头并重新初始化
    for(; loop_count < MT9V03X_SET_DATA; loop_count --)
    {
        uart_buffer[0]  = 0xA5;
        uart_buffer[1]  = buff[loop_count][0];
        temp_value      = buff[loop_count][1];
        uart_buffer[2]  = temp_value >> 8;
        uart_buffer[3]  = (uint8)temp_value;
        uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

        system_delay_ms(2);
    }

    do
    {
        if(3 <= fifo_used(camera_receiver_fifo))
        {
            uart_buffer_index = 3;
            fifo_read_buffer(camera_receiver_fifo, uart_buffer, &uart_buffer_index, FIFO_READ_AND_CLEAN);
            if((0xff == uart_buffer[1]) || (0xff == uart_buffer[2]))
            {
                return_state = 0;
                break;
            }
        }
        system_delay_ms(1);
    }while(MT9V03X_INIT_TIMEOUT > timeout_count ++);
    // 以上部分对摄像头配置的数据全部都会保存在摄像头上51单片机的eeprom中
    // 利用set_exposure_time函数单独配置的曝光数据不存储在eeprom中
    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     获取摄像头内部配置信息
// 参数说明     buff            接收配置信息的地址
// 返回参数     uint8           1-失败 0-成功
// 使用示例     mt9v03x_get_config(mt9v03x_get_confing_buffer);
// 备注信息     内部调用
//-------------------------------------------------------------------------------------------------------------------
static uint8 mt9v03x_get_config (int16 buff[MT9V03X_CONFIG_FINISH - 1][2])
{
    int8    loop_count          = 0;
    uint8   uart_buffer[4];
    uint8   return_state        = 0;
    uint16  temp_value          = 0;
    uint16  timeout_count       = 0;
    uint32  uart_buffer_index   = 0;

    switch(mt9v03x_version)
    {
        case 0x0230:    loop_count = MT9V03X_PCLK_MODE;  break;
        default:        loop_count = MT9V03X_GAIN;       break;
    }

    for(loop_count = loop_count - 1; 0 <= loop_count; loop_count --)
    {
        if((0x0230 > mt9v03x_version) && (MT9V03X_PCLK_MODE == buff[loop_count][0]))
        {
            continue;
        }
        uart_buffer[0]  = 0xA5;
        uart_buffer[1]  = MT9V03X_GET_STATUS;
        temp_value      = buff[loop_count][0];
        uart_buffer[2]  = temp_value >> 8;
        uart_buffer[3]  = (uint8)temp_value;
        uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

        timeout_count = 0;
        do
        {
            if(3 <= fifo_used(camera_receiver_fifo))
            {
                uart_buffer_index = 3;
                fifo_read_buffer(camera_receiver_fifo, uart_buffer, &uart_buffer_index, FIFO_READ_AND_CLEAN);
                buff[loop_count][1] = uart_buffer[1] << 8 | uart_buffer[2];
                break;
            }
            system_delay_ms(1);
        }while(MT9V03X_INIT_TIMEOUT > timeout_count ++);
        if(MT9V03X_INIT_TIMEOUT < timeout_count)                                // 超时
        {
            return_state = 1;
            break;
        }
    }
    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     MT9V03X UART 获取摄像头 ID
// 参数说明     void
// 返回参数     uint8           0-成功 x-失败
// 使用示例     mt9v03x_check_id();
// 备注信息     内部调用
//-------------------------------------------------------------------------------------------------------------------
static uint8 mt9v03x_uart_check_id (void)
{
    uint8   uart_buffer[4] = {0};
    uint8   return_state        = 1;
    uint16  timeout_count       = 0;
    uint32  uart_buffer_index   = 0;


    if(fifo_used(camera_receiver_fifo))
    {
        fifo_clear(camera_receiver_fifo);
    }

    uart_write_byte(MT9V03X_COF_UART, 0xFF);
    uart_buffer[0] = 0xA5;
    uart_buffer[1] = MT9V03X_COLOR_GET_WHO_AM_I;
    uart_buffer[2] = 0;
    uart_buffer[3] = 0;
    uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

    timeout_count = 0;
    do
    {
        if(3 <= fifo_used(camera_receiver_fifo))
        {
            uart_buffer_index = 3;
            fifo_read_buffer(camera_receiver_fifo, uart_buffer, &uart_buffer_index, FIFO_READ_AND_CLEAN);
            return_state = !(0x01 == uart_buffer[2] || 0x02 == uart_buffer[2]);
            break;
        }
        system_delay_ms(1);
    }while(MT9V03X_INIT_TIMEOUT > timeout_count ++);

    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     MT9V03X 通信串口回调函数
// 参数说明     void
// 返回参数     void
// 使用示例     mt9v03x_uart_handler();
// 备注信息
//-------------------------------------------------------------------------------------------------------------------
static void mt9v03x_uart_handler (void)
{
    uint8 data = 0;
    uart_query_byte(MT9V03X_COF_UART, &data);
    if(NULL != camera_receiver_fifo)
    {
        if(0xA5 == data)
        {
            fifo_clear(camera_receiver_fifo);
        }

        fifo_write_element(camera_receiver_fifo, data);
    }
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     MT9V03X摄像头场中断
// 参数说明     NULL
// 返回参数     void
//  @since      v1.0
// 使用示例     在isr.c里面先创建对应的中断函数，然后调用该函数(之后别忘记清除中断标志位)
//-------------------------------------------------------------------------------------------------------------------
void mt9v03x_dvp_handler(void)
{
    //已经修改为循环采集模式。不需要设置地址和开启DVP
    //DVP->DMA_BUF0 = (uint32)camera_buffer_addr;       // 恢复DMA地址
    mt9v03x_finish_flag = 1;                        // 摄像头采集完成标志位置1
    //已经修改为循环采集模式。不需要设置地址和开启DVP
    //DVP->CR0 |= RB_ENABLE;                          // 重新打开DVP，采集下一副图像
}




//-------------------------------------------------------------------------------------------------------------------
// 函数简介     获取摄像头固件版本
// 参数说明     void
// 返回参数     uint16          0-获取错误 N-版本号
// 使用示例     mt9v03x_get_version();                                          // 调用该函数前请先初始化串口
// 备注信息     内部调用
//-------------------------------------------------------------------------------------------------------------------
uint16 mt9v03x_get_version (void)
{
    uint8   uart_buffer[4];
    uint16  timeout_count       = 0;
    uint16  return_value        = 0;
    uint32  uart_buffer_index   = 0;

    do
    {
        uart_buffer[0] = 0xA5;
        uart_buffer[1] = MT9V03X_GET_STATUS;
        uart_buffer[2] = (uint8)((MT9V03X_GET_VERSION >> 8) & 0xFF);
        uart_buffer[3] = (uint8)(MT9V03X_GET_VERSION & 0xFF);
        uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

        do
        {
            if(3 <= fifo_used(camera_receiver_fifo))
            {
                uart_buffer_index = 3;
                fifo_read_buffer(camera_receiver_fifo, uart_buffer, &uart_buffer_index, FIFO_READ_AND_CLEAN);
                return_value = uart_buffer[1] << 8 | uart_buffer[2];
                break;
            }
            system_delay_ms(1);
        }while(MT9V03X_INIT_TIMEOUT > timeout_count ++);
    }while(0);
    return return_value;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     单独设置摄像头曝光时间
// 参数说明     light           设定曝光时间
// 返回参数     uint8           1-失败 0-成功
// 使用示例     mt9v03x_set_exposure_time(100);                 // 调用该函数前请先初始化串口
// 备注信息     设置曝光时间越大图像越亮
//              摄像头收到后会根据分辨率及FPS计算最大曝光时间如果设置的数据过大
//              那么摄像头将会设置这个最大值
//-------------------------------------------------------------------------------------------------------------------
uint8 mt9v03x_set_exposure_time (uint16 light)
{
    uint8   uart_buffer[4];
    uint8   *receiver_buffer    = NULL;
    uint8   return_state        = 0;
    uint16  temp_value          = 0;
    uint16  timeout_count       = 0;
    uint32  uart_buffer_index   = 0;

    if(MT9V03X_UART == mt9v03x_type)
    {
        do
        {
            receiver_buffer = (uint8 *)malloc(MT9V03X_COF_BUFFER_SIZE);
            if(NULL == receiver_buffer)
            {
                zf_log(0, "FIFO buffer malloc error.");
                return_state = 1;
                break;
            }
            camera_receiver_fifo = (fifo_struct *)malloc(sizeof(fifo_struct));
            if(NULL == camera_receiver_fifo)
            {
                zf_log(0, "FIFO malloc error.");
                return_state = 1;
                break;
            }
            fifo_init(camera_receiver_fifo, FIFO_DATA_8BIT, receiver_buffer, MT9V03X_COF_BUFFER_SIZE);

            uart_buffer[0]  = 0xA5;
            uart_buffer[1]  = MT9V03X_SET_EXP_TIME;
            temp_value      = light;
            uart_buffer[2]  = temp_value >> 8;
            uart_buffer[3]  = (uint8)temp_value;
            uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

            do
            {
                if(3 <= fifo_used(camera_receiver_fifo))
                {
                    uart_buffer_index = 3;
                    fifo_read_buffer(camera_receiver_fifo, uart_buffer, &uart_buffer_index, FIFO_READ_AND_CLEAN);
                    temp_value = uart_buffer[1] << 8 | uart_buffer[2];
                    break;
                }
                system_delay_ms(1);
            }while(MT9V03X_INIT_TIMEOUT > timeout_count ++);
            if((temp_value != light) || (MT9V03X_INIT_TIMEOUT <= timeout_count))
            {
                return_state = 1;
            }
        }while(0);
    }
    else
    {
        return_state = mt9v03x_sccb_set_exposure_time(light);
    }

    free(receiver_buffer);
    free(camera_receiver_fifo);
    camera_receiver_fifo = NULL;
    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     对摄像头内部寄存器进行写操作
// 参数说明     addr            摄像头内部寄存器地址
// 参数说明     data            需要写入的数据
// 返回参数     uint8           1-失败 0-成功
// 使用示例     mt9v03x_set_reg(addr, data);                    // 调用该函数前请先初始化串口
// 备注信息
//-------------------------------------------------------------------------------------------------------------------
uint8 mt9v03x_set_reg (uint8 addr, uint16 data)
{
    uint8   uart_buffer[4];
    uint8   *receiver_buffer    = NULL;
    uint8   return_state        = 0;
    uint16  temp_value          = 0;
    uint16  timeout_count       = 0;
    uint32  uart_buffer_index   = 0;

    if(MT9V03X_UART == mt9v03x_type)
    {
        do
        {
            receiver_buffer = (uint8 *)malloc(MT9V03X_COF_BUFFER_SIZE);
            if(NULL == receiver_buffer)
            {
                zf_log(0, "FIFO buffer malloc error.");
                return_state = 1;
                break;
            }
            camera_receiver_fifo = (fifo_struct *)malloc(sizeof(fifo_struct));
            if(NULL == camera_receiver_fifo)
            {
                zf_log(0, "FIFO malloc error.");
                return_state = 1;
                break;
            }
            fifo_init(camera_receiver_fifo, FIFO_DATA_8BIT, receiver_buffer, MT9V03X_COF_BUFFER_SIZE);

            uart_buffer[0]  = 0xA5;
            uart_buffer[1]  = MT9V03X_SET_ADDR;
            temp_value      = addr;
            uart_buffer[2]  = temp_value >> 8;
            uart_buffer[3]  = (uint8)temp_value;
            uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

            system_delay_ms(10);
            uart_buffer[0]  = 0xA5;
            uart_buffer[1]  = MT9V03X_SET_DATA;
            temp_value      = data;
            uart_buffer[2]  = temp_value >> 8;
            uart_buffer[3]  = (uint8)temp_value;
            uart_write_buffer(MT9V03X_COF_UART, uart_buffer, 4);

            do
            {
                if(3 <= fifo_used(camera_receiver_fifo))
                {
                    uart_buffer_index = 3;
                    fifo_read_buffer(camera_receiver_fifo, uart_buffer, &uart_buffer_index, FIFO_READ_AND_CLEAN);
                    temp_value = uart_buffer[1] << 8 | uart_buffer[2];
                    break;
                }
                system_delay_ms(1);
            }while(MT9V03X_INIT_TIMEOUT > timeout_count ++);
            if((temp_value != data) || (MT9V03X_INIT_TIMEOUT <= timeout_count))
            {
                return_state = 1;
            }
        }while(0);
    }
    else
    {
        return_state = mt9v03x_sccb_set_reg(addr, data);
    }

    free(receiver_buffer);
    free(camera_receiver_fifo);
    camera_receiver_fifo = NULL;
    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     MT9V03X SCCB 初始化
// 参数说明     void
// 返回参数     uint8           0-成功 x-失败
// 使用示例     mt9v03x_sccb_init();
// 备注信息
//-------------------------------------------------------------------------------------------------------------------
uint8 mt9v03x_sccb_init (void)
{
    uint8 return_state  = 1;

    mt9v03x_type = MT9V03X_SCCB;
    soft_iic_info_struct mt9v03x_iic_struct;
    soft_iic_init(
        &mt9v03x_iic_struct, 0,
        MT9V03X_COF_IIC_DELAY,
        MT9V03X_COF_IIC_SCL,
        MT9V03X_COF_IIC_SDA);

    if(!mt9v03x_sccb_check_id(&mt9v03x_iic_struct))
    {
        // 需要配置到摄像头的数据 不允许在这修改参数
        const int16 mt9v03x_set_confing_buffer[MT9V03X_CONFIG_FINISH][2]=
        {
            {MT9V03X_INIT,              0},                                     // 摄像头开始初始化

            {MT9V03X_AUTO_EXP,          MT9V03X_AUTO_EXP_DEF},                  // 自动曝光设置
            {MT9V03X_EXP_TIME,          MT9V03X_EXP_TIME_DEF},                  // 曝光时间
            {MT9V03X_FPS,               MT9V03X_FPS_DEF},                       // 图像帧率
            {MT9V03X_SET_COL,           MT9V03X_W},                             // 图像列数量
            {MT9V03X_SET_ROW,           MT9V03X_H},                             // 图像行数量
            {MT9V03X_LR_OFFSET,         MT9V03X_LR_OFFSET_DEF},                 // 图像左右偏移量
            {MT9V03X_UD_OFFSET,         MT9V03X_UD_OFFSET_DEF},                 // 图像上下偏移量
            {MT9V03X_GAIN,              MT9V03X_GAIN_DEF},                      // 图像增益
            {MT9V03X_PCLK_MODE,         MT9V03X_PCLK_MODE_DEF},                 // 像素时钟模式
        };
        return_state = mt9v03x_sccb_set_config(mt9v03x_set_confing_buffer);
    }

    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     MT9V03X UART 初始化
// 参数说明     void
// 返回参数     uint8           0-成功 x-失败
// 使用示例     mt9v03x_uart_init();
// 备注信息
//-------------------------------------------------------------------------------------------------------------------
uint8 mt9v03x_uart_init (void)
{
    uint8 return_state  = 1;
    uint8 loop_count    = 0;
    uint8 *receiver_buffer  = NULL;

    mt9v03x_type = MT9V03X_UART;
    do
    {
        receiver_buffer = (uint8 *)malloc(MT9V03X_COF_BUFFER_SIZE);             // 申请缓冲区
        if(NULL == receiver_buffer)                                             // 堆空间不足
        {
            zf_log(0, "FIFO buffer malloc error.");                             // 无法获取数据缓冲区提示
            return_state = 2;                                                   // 异常码
            break;
        }
        camera_receiver_fifo = (fifo_struct *)malloc(sizeof(fifo_struct));      // 申请 FIFO 对象
        if(NULL == camera_receiver_fifo)                                        // 堆空间不足
        {
            zf_log(0, "FIFO malloc error.");                                    // 无法获取 FIFO 对象提示
            free(receiver_buffer);
            return_state = 2;                                                   // 异常码
            break;
        }
        fifo_init(camera_receiver_fifo, FIFO_DATA_8BIT, receiver_buffer, MT9V03X_COF_BUFFER_SIZE);



        // 初始化串口 配置摄像头
        uart_init(MT9V03X_COF_UART, MT9V03X_COF_BAUR, MT9V03X_COF_UART_RX, MT9V03X_COF_UART_TX);
        uart_rx_interrupt(MT9V03X_COF_UART, 1);

        mt9v03x_version = mt9v03x_get_version();

        if(mt9v03x_version != 0)
        {
            if(mt9v03x_uart_check_id())
            {
                uart_rx_interrupt(MT9V03X_COF_UART, 0);
                return_state = 3;
                break;
            }
        }


        // 需要配置到摄像头的数据 不允许在这修改参数
        const int16 mt9v03x_set_confing_buffer[MT9V03X_CONFIG_FINISH][2]=
        {
            {MT9V03X_INIT,              0},                                     // 摄像头开始初始化

            {MT9V03X_AUTO_EXP,          MT9V03X_AUTO_EXP_DEF},                  // 自动曝光设置
            {MT9V03X_EXP_TIME,          MT9V03X_EXP_TIME_DEF},                  // 曝光时间
            {MT9V03X_FPS,               MT9V03X_FPS_DEF},                       // 图像帧率
            {MT9V03X_SET_COL,           MT9V03X_W},                             // 图像列数量
            {MT9V03X_SET_ROW,           MT9V03X_H},                             // 图像行数量
            {MT9V03X_LR_OFFSET,         MT9V03X_LR_OFFSET_DEF},                 // 图像左右偏移量
            {MT9V03X_UD_OFFSET,         MT9V03X_UD_OFFSET_DEF},                 // 图像上下偏移量
            {MT9V03X_GAIN,              MT9V03X_GAIN_DEF},                      // 图像增益
            {MT9V03X_PCLK_MODE,         MT9V03X_PCLK_MODE_DEF},                 // 像素时钟模式
        };

        // 从摄像头内部获取到的配置数据 不允许在这修改参数
        int16 mt9v03x_get_confing_buffer[MT9V03X_CONFIG_FINISH - 1][2]=
        {
            {MT9V03X_AUTO_EXP,          0},                                     // 自动曝光设置
            {MT9V03X_EXP_TIME,          0},                                     // 曝光时间
            {MT9V03X_FPS,               0},                                     // 图像帧率
            {MT9V03X_SET_COL,           0},                                     // 图像列数量
            {MT9V03X_SET_ROW,           0},                                     // 图像行数量
            {MT9V03X_LR_OFFSET,         0},                                     // 图像左右偏移量
            {MT9V03X_UD_OFFSET,         0},                                     // 图像上下偏移量
            {MT9V03X_GAIN,              0},                                     // 图像增益
            {MT9V03X_PCLK_MODE,         0},                                     // 像素时钟模式命令 PCLK模式 < 仅总钻风 MT9V034 V1.5 以及以上版本支持该命令 >
        };

        if(mt9v03x_set_config(mt9v03x_set_confing_buffer))                      // 设置总钻风配置
        {
            // 如果程序在输出了断言信息 并且提示出错位置在这里
            // 那么就是串口通信出错并超时退出了
            // 检查一下接线有没有问题 如果没问题可能就是坏了
            zf_log(0, "MT9V03X set config error.");
            uart_rx_interrupt(MT9V03X_COF_UART, 0);
            return_state = 1;
            break;
        }

        // 获取配置便于查看配置是否正确
        if(mt9v03x_get_config(mt9v03x_get_confing_buffer))
        {
            // 如果程序在输出了断言信息 并且提示出错位置在这里
            // 那么就是串口通信出错并超时退出了
            // 检查一下接线有没有问题 如果没问题可能就是坏了
            zf_log(0, "MT9V03X get config error.");
            uart_rx_interrupt(MT9V03X_COF_UART, 0);
            return_state = 1;
            break;
        }

        for(loop_count = 0; MT9V03X_CONFIG_FINISH - 1 > loop_count; loop_count ++)
        {
            if( mt9v03x_set_confing_buffer[loop_count + 1][0] != mt9v03x_get_confing_buffer[loop_count][0] ||
                mt9v03x_set_confing_buffer[loop_count + 1][1] != mt9v03x_get_confing_buffer[loop_count][1])
            {
                break;
            }
        }
        return_state = (MT9V03X_CONFIG_FINISH - 2 <= loop_count) ? 0 : 1;
    }while(0);

    free(receiver_buffer);
    free(camera_receiver_fifo);
    camera_receiver_fifo = NULL;

    return return_state;
}

//-------------------------------------------------------------------------------------------------------------------
// 函数简介     MT9V03X 摄像头初始化
// 参数说明     void
// 返回参数     uint8           0-成功 x-失败
// 使用示例     mt9v03x_init();
// 备注信息
//-------------------------------------------------------------------------------------------------------------------
uint8 mt9v03x_init (void)
{

    uint8 return_state  = 0;

    do
    {
        set_camera_type(CAMERA_GRAYSCALE, NULL, mt9v03x_dvp_handler);
        if(mt9v03x_sccb_init())
        {
            set_camera_type(CAMERA_GRAYSCALE, mt9v03x_uart_handler, mt9v03x_dvp_handler);
            return_state = mt9v03x_uart_init();
        }

        if(!return_state)
        {
           // DVP引脚初始化
            dvp_gpio_init(
                MT9V03X_D0_PIN, MT9V03X_D1_PIN, MT9V03X_D2_PIN, MT9V03X_D3_PIN,
                MT9V03X_D4_PIN, MT9V03X_D5_PIN, MT9V03X_D6_PIN, MT9V03X_D7_PIN,
                MT9V03X_PCLK_PIN, MT9V03X_VSY_PIN, MT9V03X_HERF_PIN);

            // DVP接口初始化
            dvp_camera_init((uint32 *)&mt9v03x_image[0], (uint32 *)&mt9v03x_image[0], MT9V03X_W*MT9V03X_H, MT9V03X_H);
            break;
        }
        set_camera_type(NO_CAMERE, NULL, NULL);
    }while(0);

    return return_state;
}
