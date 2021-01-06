import plotly.express as px


def line_plot(data, x, y, title, label, template):
    fig = px.line(data, x=x, y=y, title=title, labels=label, template=template)
    return fig


def bar_plot(data, x, y, title, label, template):
    fig = px.bar(data, x=x, y=y, title=title, labels=label, template=template)
    return fig


def histogram_plot(data, x, y, title, label, template):
    fig = px.histogram(data, x=x, y=y, title=title, labels=label, template=template)
    return fig


def area_plot(data, x, y, title, label, template):
    fig = px.area(data, x=x, y=y, title=title, labels=label, template=template)
    return fig


def funnel_plot(data, x, y, title, label, template):
    fig = px.funnel(data, x=x, y=y, title=title, labels=label, template=template)
    return fig


def scatter_plot(data, x, y, title, label, template):
    fig = px.funnel(data, x=x, y=y, title=title, labels=label, template=template)
    return fig

