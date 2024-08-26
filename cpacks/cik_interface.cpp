#include <Python.h>
#include <stdlib.h>
#include <iostream>

typedef struct {
    PyObject_HEAD
    int _test_value;
} CikObject;

// function dealloc
static void CikObject_dealloc(CikObject* self) {
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* CikObject_new(PyTypeObject *type, PyObject *args, PyObject *kwargs) {

}