#include <Python.h>
#include <stdlib.h>
#include <iostream>

typedef struct {
    PyObject_HEAD
    int value;
} CikObject;

// function dealloc
static void CikObject_dealloc(CikObject* self) {
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* CikObject_new(PyTypeObject *type, PyObject *args, PyObject *kwargs) {

    CikObject *self;
    self = (CikObject *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->value = 0;
    }
    return (PyObject *)self;
}