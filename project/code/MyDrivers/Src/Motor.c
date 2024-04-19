 /**
  ******************************************************************************
  * @file    Motor.c
  * @author  ׯ�ı�
  * @brief   �������
  * @date    2/11/2023
    @verbatim

    ��·�������

    @endverbatim
  * @{
**/

/* Includes ------------------------------------------------------------------*/
#include "Motor.h"

/* Define\Declare ------------------------------------------------------------*/
//#define PWM_Freq 17000
//#define Motor_LF PWM2_MODULE2_CHB_C11
//#define Motor_RF PWM1_MODULE0_CHA_D12//ǰ��
//#define Motor_RB PWM4_MODULE2_CHA_C30 //
//#define Motor_LB PWM1_MODULE1_CHB_D15
//#define Motor_Dir_LF C31
//#define Motor_Dir_RF D13
//#define Motor_Dir_LB D14
//#define Motor_Dir_RB C27
#define PWM_Freq 17000
#define Motor_LF           A0 //ǰ�� PWM1
#define Motor_RF           A3 //    PWM2
#define Motor_LB           D13//ת�� PWM3
#define Motor_RB           D14//

#define Motor_Dir_LF A1   //DIR1
#define Motor_Dir_RF A2
#define Motor_Dir_LB D12
#define Motor_Dir_RB D15


/**
 ******************************************************************************
 *  @defgroup �ⲿ����
 *  @brief
 *
**/

/**@brief     �����ʼ��
-- @param     ��
-- @auther    ׯ�ı�
-- @date      2023/11/2
**/
void Motor_Init()
{
    //ǰ���������
    pwm_init(Motor_LF,PWM_Freq,0);
    pwm_init(Motor_LB,PWM_Freq,0);
    pwm_init(Motor_RF,PWM_Freq,0);
    pwm_init(Motor_RB,PWM_Freq,0);

    gpio_init(Motor_Dir_LF,GPO,1,GPO_PUSH_PULL);
    gpio_init(Motor_Dir_RF,GPO,1,GPO_PUSH_PULL);
    gpio_init(Motor_Dir_LB,GPO,1,GPO_PUSH_PULL);
    gpio_init(Motor_Dir_RB,GPO,1,GPO_PUSH_PULL);
}

/**@brief     ����ٶ�����
-- @param     MotorHandle Motor ѡ�����ҵ��
-- @param     uint16 PWMDuty PWM��ռ�ձȣ���Ӧ0-100���ٶ�
-- @auther    ׯ�ı�
-- @date      2023/11/2
**/
void Set_Motor_Speed(MotorHandle Motor, float PWMDuty)
{
    
    int Forward = 0;
    double Pwm_Temp = 0;
    double Pwm_Set = 0;
    //�ж������PWM������
    if(PWMDuty < 0)
    {
        Pwm_Temp = -PWMDuty;
        Forward = 0;
    }
    else if(PWMDuty >= 0)
    {
        Pwm_Temp = PWMDuty;
        Forward = 1;
    }

    Pwm_Set = Pwm_Temp *100.0;//��һ��

    if(Pwm_Set > 10000)//�޷�
    {
        Pwm_Set = 9999;
    }

    switch (Motor)
    {
        case LMotor_F:
            if(Forward)
            {
                pwm_set_duty(Motor_LF,Pwm_Set);
                gpio_set_level(Motor_Dir_LF,0);
            }
            else if(!Forward)
            {
                pwm_set_duty(Motor_LF,Pwm_Set);
                gpio_set_level(Motor_Dir_LF,1);
            }
        break;
        case RMotor_B:
            if(Forward)
            {
                pwm_set_duty(Motor_RB,Pwm_Set);
                gpio_set_level(Motor_Dir_RB,1);
            }
            else if(!Forward)
            {
                pwm_set_duty(Motor_RB,Pwm_Set);
                gpio_set_level(Motor_Dir_RB,0);
            }
        break;
        case RMotor_F:
            if(Forward)
            {
                pwm_set_duty(Motor_RF,Pwm_Set);
                gpio_set_level(Motor_Dir_RF,1);
            }
            else if(!Forward)
            {
                pwm_set_duty(Motor_RF,Pwm_Set);
                gpio_set_level(Motor_Dir_RF,0);
            }
        break;
        case LMotor_B:
            if(Forward)
            {
                pwm_set_duty(Motor_LB,Pwm_Set);
                gpio_set_level(Motor_Dir_LB,1);
            }
            else if(!Forward)
            {
                pwm_set_duty(Motor_LB,Pwm_Set);
                gpio_set_level(Motor_Dir_LB,0);
            }
        break;
        default:
        break;
    }
}

/**@brief     ���ʧ��
-- @param     ��
-- @auther    ׯ�ı�
-- @date      2024/3/13
**/
void Motor_Disable()
{
    Set_Motor_Speed(LMotor_F,0);
    Set_Motor_Speed(LMotor_B,0);
    Set_Motor_Speed(RMotor_F,0);
    Set_Motor_Speed(RMotor_B,0);
    // printf("Motor_Disable\r\n");
}