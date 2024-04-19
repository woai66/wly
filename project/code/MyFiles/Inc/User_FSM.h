#ifndef USERFSM_H_
#define USERFSM_H_

#include "FSM.h"
#include "UserMain.h"

enum State  //״̬
{
    Depart = 0,//����
    LinePatrol = 1,//Ѳ��
    FindBoard = 2,//�ҵ���Ƭ
};

enum Board_State
{
    Find_Left,//�ҵ���߿�Ƭ
    Wait_Data,//�ȴ�����
    Move_Left,//�ƶ�����Ƭǰ��
    Confirm_Left,//ȷ���Ƿ��ƶ���λ
    Return_Line,
    Finish,//
};


void My_FSM_Init();
extern FSM_t *CURRENT_FSM;//��ǰ����״̬��

#endif