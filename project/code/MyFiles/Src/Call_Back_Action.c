/**
  ******************************************************************************
  * @file    Callback_Action.c
  * @author  ׯ�ı�
  * @brief   �ص�����
  * @date    11/4/2023
  * 
    @verbatim
    ������Ҫ���ж�ִ�еĺ�����������һ�ļ�
    @endverbatim
  * @{
**/

/* Includes ------------------------------------------------------------------*/
#include "Call_Back_Action.h"
#include "zf_common_headfile.h"
#include "UserMain.h"

/* Define\Declare ------------------------------------------------------------*/
#define Sensor_CH                  (TIM10_PIT)// ʹ�õ������жϱ�� ����޸� ��Ҫͬ����Ӧ�޸������жϱ���� isr.c �еĵ���
#define Sensor_PRIORITY            (TIM7_IRQn)// ��Ӧ�����жϵ��жϱ��
#define  PIT_CH1 (TIM1_PIT)
#define  PIT_CH2 (TIM2_PIT)

/**
 ******************************************************************************
 *  @defgroup �ⲿ����
 *  @brief
 *
**/

/**@brief   ��ʱ����ʼ��
-- @param   ��
-- @auther  ׯ�ı�
-- @date    2023/11/4
**/
void TIM_Init()
{
    pit_ms_init(Sensor_CH, 5);                                                  // ��ʼ�� PIT_CH0 Ϊ�����ж� 5ms ����
    interrupt_set_priority(Sensor_PRIORITY, 0); 
    pit_ms_init(PIT_CH1, 10);                                                  // ��ʼ�� PIT_CH1 Ϊ�����ж� 15ms ����
    pit_ms_init(PIT_CH2, 15);                                                  // ��ʼ�� PIT_CH2 Ϊ�����ж� 10ms ����
}


/**@brief   �������жϺ���
-- @param   ��
-- @auther  ׯ�ı�
-- @date    2023/11/4
**/
void Sensor_Handler()
{
    Gyro_Get_All_Angles();
    Encoder_Process();
}

/**@brief   ��Ŀ���openart����
-- @param   ��
-- @auther  ������
-- @date    2023/12/23
**/
void Uart_Findborder_Receive(void)
{
	
    uart_query_byte(UART_1, &_UART_FINDBORDER.get_data);
    fifo_write_buffer(&_UART_FINDBORDER.uart_data_fifo, &_UART_FINDBORDER.get_data, 1);
	if (_UART_FINDBORDER.get_data == 0x80)
    {
      UnpackFlag.FINDBORDER_DATA_FLAG = true;
    }
}

/**@brief   ΢��openart����
-- @param   ��
-- @auther  ������
-- @date    2023/12/23
**/
void Uart_Fine_Tuning_Receive(void)
{
	static uint8_t lastData;
    uart_query_byte(UART_2, &_UART_FINE_TUNING.get_data);
	_UART_FINE_TUNING.fifo_get_data[_UART_FINE_TUNING.index] = _UART_FINE_TUNING.get_data;
	_UART_FINE_TUNING.index++;
	
    // fifo_write_buffer(&_UART_FINE_TUNING.uart_data_fifo, &_UART_FINE_TUNING.get_data, 1);
	// printf("%x  \n", _UART_FINE_TUNING.get_data);
	if(_UART_FINE_TUNING.get_data == 0xbf && lastData == 0xfc)
    {
	  /*
	  printf("+++++++++++++++++\n");
	  
	  for (uint32_t i = 0; i < _UART_FINE_TUNING.index; i++)
	  {
		printf("%x \n", _UART_FINE_TUNING.fifo_get_data[i]);
	  }
	  */
	  // ���ֽ�ת������
	  FINETUNING_DATA.dx = (float)((_UART_FINE_TUNING.fifo_get_data[1] >> 7) == 0) ? ((_UART_FINE_TUNING.fifo_get_data[0] + (_UART_FINE_TUNING.fifo_get_data[1] << 8))) : (-(65536 - (_UART_FINE_TUNING.fifo_get_data[0] + (_UART_FINE_TUNING.fifo_get_data[1] << 8))));
	  FINETUNING_DATA.dy = (float)((_UART_FINE_TUNING.fifo_get_data[3] >> 7) == 0) ? ((_UART_FINE_TUNING.fifo_get_data[2] + (_UART_FINE_TUNING.fifo_get_data[3] << 8))) : (-(65536 - (_UART_FINE_TUNING.fifo_get_data[2] + (_UART_FINE_TUNING.fifo_get_data[3] << 8))));
	  FINETUNING_DATA.FINETUNING_FINISH_FLAG = (_UART_FINE_TUNING.fifo_get_data[4] == 0x01) ? (true) : (false);
	  // printf("dx:%f dy:%f tuning: %d \n", FINETUNING_DATA.dx, FINETUNING_DATA.dy,  FINETUNING_DATA.FINETUNING_FINISH_FLAG);
	  // printf("+++++++++++++++++\n");
	  memset(_UART_FINE_TUNING.fifo_get_data, 0, sizeof(_UART_FINE_TUNING.fifo_get_data));
	  _UART_FINE_TUNING.index = 0;
      // UnpackFlag.FINETUNING_DATA_FLAG = true;
    }
	lastData = _UART_FINE_TUNING.get_data;
}