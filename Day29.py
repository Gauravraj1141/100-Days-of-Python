jk = '''{'authentication_params': {'user_profile_id': '982f23e3-73c5-4068-af87-490b13e1fe69', 'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5IjoiRy1LYVBkU2dWa1lwMnM1djh5L0I_RShIK01iUWVUaFdtWnE0dDZ3OXokQyZGKUpATmNSZlVqWG4ycjV1OHghQSIsInVzZXJfcHJvZmlsZV9pZCI6Ijk4MmYyM2UzLTczYzUtNDA2OC1hZjg3LTQ5MGIxM2UxZmU2OSIsInNlc3Npb25faWQiOiJjNjU3ODMwNC0xOGVmLTQ1MGUtYTYxMS0xMmRlYzEwY2EzNmQiLCJleHAiOjE2NzUxNzA4NTcsImlhdCI6MTY3NDMwNjczN30.cB4e6vIlBCi83AM6gskoqTpFCyGieDZ0k9V2XDMlm1g'}, 'payload': {'notification_text': 'congrates your property added successfully for more informartion please on this link ', 'notification_status': '1', 'notification_type': '1', 'redirection_page': 'tenantowner/servicelayer/notification', 'redirection_id': '34svsdfe3-4036-403d-bf84-cf8400f67836'}, 'token_user_profile_id': '982f23e3-73c5-4068-af87-490b13e1fe69', 'session_id': 'c6578304-18ef-450e-a611-12dec10ca36d', 'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5IjoiRy1LYVBkU2dWa1lwMnM1djh5L0I_RShIK01iUWVUaFdtWnE0dDZ3OXokQyZGKUpATmNSZlVqWG4ycjV1OHghQSIsInVzZXJfcHJvZmlsZV9pZCI6Ijk4MmYyM2UzLTczYzUtNDA2OC1hZjg3LTQ5MGIxM2UxZmU2OSIsInNlc3Npb25faWQiOiJjNjU3ODMwNC0xOGVmLTQ1MGUtYTYxMS0xMmRlYzEwY2EzNmQiLCJleHAiOjE2NzQ4OTQ5NzEsImlhdCI6MTY3NDg5NDM3MX0._wQYpJ7yfEgHAlnECnRMlH73F5pyBjTgxVKNPtb4_qg', 'service_name': 'generate_all_notifications', 'service_request_id': UUID('6bfd0543-9ee5-11ed-b2c2-c8e265cdbe81')}'''

ram = "rana ji"
input_json = dict(zip(['authentication_params', 'payload'], [{'user_profile_id': ram, 'refresh_token': ""},
                                                             {'notification_text': '', 'notification_status': '',
                                                              'notification_type': '', 'redirection_page': '',
                                                              'redirection_id': ''}]))
# input_json['authentication_params']['user_profile_id'] = '982f23e3-73c5-4068-af87-490b13e1fe69'
input_json['authentication_params'][
    'refresh_token'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5IjoiRy1LYVBkU2dWa1lwMnM1djh5L0I_RShIK01iUWVUaFdtWnE0dDZ3OXokQyZGKUpATmNSZlVqWG4ycjV1OHghQSIsInVzZXJfcHJvZmlsZV9pZCI6Ijk4MmYyM2UzLTczYzUtNDA2OC1hZjg3LTQ5MGIxM2UxZmU2OSIsInNlc3Npb25faWQiOiJjNjU3ODMwNC0xOGVmLTQ1MGUtYTYxMS0xMmRlYzEwY2EzNmQiLCJleHAiOjE2NzUxNzA4NTcsImlhdCI6MTY3NDMwNjczN30.cB4e6vIlBCi83AM6gskoqTpFCyGieDZ0k9V2XDMlm1g'
input_json['payload']['notification_text'] = "Hey congratulations your property has been successfully added "
input_json['payload']['notification_status'] = "1"
input_json['payload']['notification_type'] = "1"
input_json['payload']['redirection_page'] = "tenantowner/servicelayer/notification"
input_json['payload']['redirection_id'] = "34svsdfe3-4036-403d-bf84-cf8400f67836"

najim_json = {
    'authentication_params': {
        "user_profile_id": ram
    },
    'payload': {
        'notification_text': "this is for my ownow",
        'notification_status': "1",
        'notification_type': "1",
        'redirection_page': "tenantowner/servicelayer/notification",
        'redirection_id': "34svsdfe3-4036-403d-bf84-cf8400f67836",
    }
}

# print(input_json)
print(najim_json)

# print(jk)




