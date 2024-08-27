#include "include/Python.h"
//#include "glfw_include/glad/glad.h"
//#include "glfw_include/GLFW/glfw3.h"
#include <stdlib.h>
#include <iostream>
#include "yikmodsmodules/insane.h"
#include "yikmodsmodules/utils.h"
static PyObject* method_test(PyObject* self, PyObject* args) {

    fuck();
    return PyLong_FromLong(1);
}

static PyObject* method_sleep(PyObject* self, PyObject* args) {
    long long int toSleep = NULL;
    bool force = false;
    if (!PyArg_ParseTuple(args, "L|p", &toSleep, &force)) {
        return NULL;
    }
    //    printf("%lld",realVal);
    if (force) {
        cysleep_force(toSleep);
    }
    else { cysleep(toSleep); }
    return PyLong_FromLong(1);

}

static PyObject* method_initialize(PyObject* self, PyObject* args) {

    bool ret = glfwInit();
    return PyBool_FromLong(ret);
}


static PyMethodDef CynamicsMethods[] = {
    {"sleep", method_sleep, METH_VARARGS, "Testing if Cynamics is loaded"},
    {"test", method_test,METH_VARARGS, "Sleep for {x} milliseconds"},
    {"init",method_initialize,METH_VARARGS,"Initialize GLFW"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef cynamicsmodule = {
    PyModuleDef_HEAD_INIT,
    "cikmods",
    "Cpp YikPok",
    -1,
    CynamicsMethods
};

PyMODINIT_FUNC PyInit_cikmods(void) {
    return PyModule_Create(&cynamicsmodule);
}