/**
  ******************************************************************************
  * @file    UserMain.c
  * @author  ׯ�ı�
  * @brief   ������
  *
    @verbatim
    ȫ����ʼ������д��UserInit�У�������while������д��UserLoop��
    @endverbatim
  * @{
**/

/* Includes ------------------------------------------------------------------*/
#include "UserMain.h"
#include "zf_common_headfile.h"
#include "User_FSM.h"

/* Define\Declare ------------------------------------------------------------*/
uint16 Start = 2;
uint8 Once = 1;
/**
 ******************************************************************************
 *  @defgroup �ڲ�����
 *  @brief
 *
 **/
void IMU_Init()
{
    while (1)
    {
        if (imu660ra_init())
            tft180_show_string(Row_0, Row_0, "IMU reinit.");
        else
            break;
        system_delay_ms(1000);
    }
    system_delay_ms(100);
    tft180_show_string(Row_0, Line_0, "IMU Init ...");
    Gyro_Offset_Init();
}

void Mt9v03x_Init()
{
    while (1)
    {
        if (mt9v03x_init())
            tft180_show_string(0, 16, "mt9v03x reinit.");
        else
            break;
        system_delay_ms(1000); // ���Ʊ�ʾ�쳣
    }
//    tft180_show_string(Row_0, Line_1, "Mt9v03x Init ...");
}

/**
 ******************************************************************************
 *  @defgroup �ⲿ����
 *  @brief
 *
 **/

/**@brief   ���г�ʼ������
-- @param   ��
-- @auther  ׯ�ı�
-- @date    2023/11/4
**/
void User_Init()
{
    system_delay_ms(100);//��ʱһ��ȴ����������ϵ�
    tft180_init();
//    IMU_Init();
     Mt9v03x_Init();
     timer_init(TIM_1,TIMER_MS);
//    All_Encoder_Init();
//    tft180_show_string(Row_0, Line_2, "Encoder Init ...");
//    Rotary_Init();
//    Bluetooth_Init();
//    tft180_show_string(Row_0, Line_3, "Rotary Init ...");
//    Manipulator_Init();
//    Motor_Init();
//    tft180_show_string(Row_0, Line_4, "Motor Init ...");
//    Beep_Init();
//    // dl1a_init();
//    All_PID_Init();
//    // Flash_Init();
//    UART_Init();
//    My_FSM_Init();
//    tft180_show_string(Row_0, Line_5, "Soft Init ...");
//    tft180_clear();
//    system_delay_ms(1000);
//    TIM_Init();
//    timer_init(TIM_1, TIMER_MS);
    // Beep(On);
    
    // Beep(Off);
}
/**@brief   ������ѭ������
-- @param   ��
-- @auther  ׯ�ı�
-- @date    2023/9/12
**/
void User_Loop()
{
    timer_start(TIM_1);
    Image_Process();
    timer_stop(TIM_1);
    Menu_Display();
    timer_clear(TIM_1);
}