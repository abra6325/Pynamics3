
#include <Python.h>
//#include "GLFW/glfw3.h"
//#include "glad/gl.h"
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

static PyObject *method_init(PyObject *self,PyObject *args){
//    if(!glfwInit()){
//
//    }
    return PyLong_FromLong(1);
}



static PyMethodDef CynamicsMethods[] = {
    {"sleep", method_sleep, METH_VARARGS, "Testing if Cynamics is loaded"},
    {"test", method_test,METH_VARARGS, "Sleep for {x} milliseconds"},
    {"init", method_init,METH_VARARGS, "Initialize GLFW"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef cynamicsmodule = {
    PyModuleDef_HEAD_INIT,
    "cik_core",
    "Cpp YikPok",
    -1,
    CynamicsMethods
};

PyMODINIT_FUNC PyInit_cik_core(void) {
    return PyModule_Create(&cynamicsmodule);
}