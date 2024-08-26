
#include <Python.h>
#include <stdlib.h>
#include <iostream>
#include "cynmodmodules/insane.h"
#include "cynmodmodules/utils.h"
static PyObject *method_test(PyObject *self, PyObject *args) {

    fuck();
    return PyLong_FromLong(1);
}

static PyObject *method_sleep(PyObject *self,PyObject *args){
    long long int toSleep = NULL;
    bool force = false;
    if (!PyArg_ParseTuple(args, "L|p", &toSleep,&force)) {
        return NULL;
    }
//    printf("%lld",realVal);
    if(force){
        cysleep_force(toSleep);
    }
    else {cysleep(toSleep);}
    return PyLong_FromLong(1);
}


static PyMethodDef CynamicsMethods[] = {
    {"sleep", method_sleep, METH_VARARGS, "Testing if Cynamics is loaded"},
    {"test", method_test,METH_VARARGS, "Sleep for {x} milliseconds"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef cynamicsmodule = {
    PyModuleDef_HEAD_INIT,
    "cynamics",
    "Cpp Pynamics",
    -1,
    CynamicsMethods
};

PyMODINIT_FUNC PyInit_cynamics(void) {
    return PyModule_Create(&cynamicsmodule);
}