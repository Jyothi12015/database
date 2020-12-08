from datetime import datetime
def configure_template_methods(app):
    @app.template_filter('formatdatetime')
    def format_datetime(value,format="%d %b %Y %I:%M %p"):
        if value is None:
            return ""
        if isinstance(value,int):
            value=datetime.fromtimestamp(value)
            return value.strftime(format)
        else:
            return value