#include <Python.h>
#include <stdlib.h>
#include <iostream>

typedef struct {
    PyObject_HEAD

    PyObject* parent;   // parent: Any[CikObject, None]
    PyObject* children; // children: List[CikObject]

} CikObject;
// function dealloc
static void CikObject_dealloc(CikObject* self) {
    //decrement reference vectors.
    Py_XDECREF(self->parent);
    Py_XDECREF(self->children);
    Py_TYPE(self)->tp_free((PyObject*)self);
}
static PyObject* CikObject_new(PyTypeObject *type, PyObject *args, PyObject *kwargs) {
    CikObject *self;
    self = (CikObject *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->parent = Py_None;
        Py_INCREF(Py_None);
        self->children = PyList_New(0);
        if (self->children == NULL) { // auto self-destruct on malfunction init
            Py_DECREF(self);
            return NULL;
        }
    }
    return (PyObject *) self;
}
// @property : parent
static PyObject* CikObject_get_parent_INVISIBLE(CikObject *self, void *closure) {
    return self->parent;
}
static int CikObject_set_parent_INVISIBLE(CikObject *self, PyObject *parent, void *closure) {
    self->parent = parent;
    return 0;
}
static PyObject* CikObject_get_children_INVISIBLE(CikObject* self, void *closure) {
    return self->children;
}
static PyGetSetDef CikObject_getset[] = {
    {"parent",   (getter) CikObject_get_parent_INVISIBLE, (setter) CikObject_set_parent_INVISIBLE, "The parent of this object", NULL},
    {"children", (getter) CikObject_get_children_INVISIBLE, NULL, "The parent of this object", NULL},
    {NULL}
};
static PyObject *
CikObject_add_child(CikObject *self, PyObject *args)
{
    PyObject *child;
    if (!PyArg_ParseTuple(args, "O", &child)) {
        return NULL;
    }
    if (PyList_Append(self->children, child) < 0) {
        return NULL;
    }
    Py_RETURN_NONE;
}

// BODY INIT
static PyMethodDef CikObject_methods[] = {
    {"add_child", (PyCFunction) CikObject_add_child, METH_VARARGS, "Adds a children"},
    {NULL}  /* Sentinel */
};

static PyTypeObject CikObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "cik_core.CikObject",               /* tp_name */
    sizeof(CikObject),           /* tp_basicsize */
    0,                               /* tp_itemsize */
    (destructor)CikObject_dealloc,     /* tp_dealloc */
    0,                               /* tp_print */
    0,                               /* tp_getattr */
    0,                               /* tp_setattr */
    0,                               /* tp_reserved */
    0,                               /* tp_repr */
    0,                               /* tp_as_number */
    0,                               /* tp_as_sequence */
    0,                               /* tp_as_mapping */
    0,                               /* tp_hash  */
    0,                               /* tp_call */
    0,                               /* tp_str */
    0,                               /* tp_getattro */
    0,                               /* tp_setattro */
    0,                               /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,              /* tp_flags */
    "Cik object",                /* tp_doc */
    0,                               /* tp_traverse */
    0,                               /* tp_clear */
    0,                               /* tp_richcompare */
    0,                               /* tp_weaklistoffset */
    0,                               /* tp_iter */
    0,                               /* tp_iternext */
    CikObject_methods,                 /* tp_methods */
    0,                               /* tp_members */
    CikObject_getset,                               /* tp_getset */
    0,                               /* tp_base */
    0,                               /* tp_dict */
    0,                               /* tp_descr_get */
    0,                               /* tp_descr_set */
    0,                               /* tp_dictoffset */
    0,                               /* tp_init */
    0,                               /* tp_alloc */
    CikObject_new,                     /* tp_new */
};






