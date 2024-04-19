#ifndef USERFSM_H_
#define USERFSM_H_

#include "FSM.h"
#include "UserMain.h"

enum State  //状态
{
    Depart = 0,//发车
    LinePatrol = 1,//巡线
    FindBoard = 2,//找到卡片
};

enum Board_State
{
    Find_Left,//找到左边卡片
    Wait_Data,//等待数据
    Move_Left,//移动到卡片前面
    Confirm_Left,//确认是否移动到位
    Return_Line,
    Finish,//
};


void My_FSM_Init();
extern FSM_t *CURRENT_FSM;//当前运行状态机

#endif