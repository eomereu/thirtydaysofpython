import os

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("Template path is invalid! (%s)" %(file_path))
    else:
        return os.path.join(os.getcwd(), path)

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def render_context(template_string, context):
    return template_string.format(**context)

# path of message 01 and itself
template_path = "Templates/emailMessage.txt"
template = get_template(template_path)

template_html_path = "Templates/emailMessage.html"
template_html = get_template(template_html_path)
context = {
    "name": "Justin",
    "date": None,
    "amount": None
}

print(render_context(template, context))
print(render_context(template_html, context))