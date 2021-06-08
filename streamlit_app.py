import streamlit as st
import streamlit.components.v1 as components
import os

_RELEASE = False
COMPONENT_NAME = "terminal"

if not _RELEASE:
    _component_func = components.declare_component(
        COMPONENT_NAME,
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(COMPONENT_NAME, path=build_dir)


def ark_terminal():
    return _component_func()


# Setting page appearance to "Wide Mode"
st.set_page_config(layout="wide")

if not _RELEASE:
    ark_terminal()
