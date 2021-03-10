# File: pipl_view.py
# Copyright (c) 2018-2021 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.


def get_ctx_result(result):

    ctx_result = {}
    param = result.get_param()
    summary = result.get_summary()
    data = result.get_data()

    ctx_result['param'] = param
    ctx_result['status'] = result.get_status()
    ctx_result['message'] = result.get_message()

    if (summary):
        ctx_result['summary'] = summary

    if (not data):
        return ctx_result

    ctx_result['data'] = data[0] or list()

    return ctx_result


def display_person_info(provides, all_app_runs, context):

    context['results'] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:
            ctx_result = get_ctx_result(result)
            if (not ctx_result):
                continue
            results.append(ctx_result)

    return 'display_person_info.html'
