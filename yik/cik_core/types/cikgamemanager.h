#include <Python.h>
#include <stdlib.h>
#include <iostream>
#include "cikobject.h"
#include "../cynmodmodules/utils.h"
typedef struct{
    CikObject cik,
    int tps,
    long long tick
} GameManagerObject;

static PyObject * GameManagerObject_start(GameManagerObject *self, PyObject *args){ //GAME MANAGER START TICK.
    long long tps = self->tps;
    float tps_epoch = (long long) 1 / tps;
    long long toSleep = (long long) (tps_epoch * 1000000000);

    while(true){
        cysleep_force(toSleep);
        // TODO
        std::cout<<"GAME TICK"<<std::endl;
    }
}
static int GameManagerObject_init(GameManagerObject *self, PyObject *args, PyObject *kwds){

}
