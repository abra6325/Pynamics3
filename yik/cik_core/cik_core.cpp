
#include <Python.h>
//#include "GLFW/glfw3.h"
//#include "glad/gl.h"
#include <stdlib.h>
#include <iostream>
#include "cynmodmodules/insane.h"
#include "cynmodmodules/utils.h"
#include "types/cikobject.h"

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
    PyObject* m;
    if (PyType_Ready(&CikObject_Type) < 0)
        return NULL;
    m = PyModule_Create(&cynamicsmodule);
    if (m == NULL)
        return NULL;
    // object initialization
    Py_INCREF(&CikObject_Type);
    PyModule_AddObject(m, "CikObject", (PyObject*) & CikObject_Type); //
    return m;
}
//6f686026-a75a-46a4-b5cb-b495d3e5560c
//ee34d4ac-eb50-476e-b271-eed4cb559d9a
//6df6a05c-789a-402d-afcf-ef5ec5ec63a7