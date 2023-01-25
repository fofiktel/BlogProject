# def get_upload_filename(upload_name, request):
#     referrer = request.META.get('HTTP_REFERER')
#     http_origin = request.META.get('HTTP_ORIGIN') + "/"
#     referrer = referrer.replace(http_origin, "")
#     print(referrer, http_origin)
#     return f'{referrer}/{upload_name}'