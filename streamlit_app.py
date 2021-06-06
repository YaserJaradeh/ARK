import streamlit as st
import streamlit.components.v1 as components
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")

_terminal = components.declare_component(
    "terminal", path=build_dir
)


def ark_terminal():
    return _terminal()


ark_terminal()
