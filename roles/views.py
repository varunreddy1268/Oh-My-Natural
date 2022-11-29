from django.shortcuts import render, redirect
from roles.models import User
import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from roles.db_tables import CreateTable, insert_user, check_login, all_flights_in_db, update_flight_time,\
    get_all_gates_information, is_already_exist, setup_gates, insert_flights_gates, free_gate
CreateTable()


@require_http_methods(["GET", "POST"])
def register_user(request):
    req_body = json.loads(request.body.decode('utf-8'))
    f_name = req_body.get('first_name')
    l_name = req_body.get('last_name')
    email = req_body.get('email')
    password = req_body.get('password')
    if is_already_exist(email):
        return HttpResponse(json.dumps({'msg': 'User already exist'}))
    user = insert_user(f_name, l_name, email, password)
    if user:
        return HttpResponse(json.dumps({'msg': 'User has been registered'}))
    else:
        return HttpResponse(json.dumps({'msg': 'error'}))


def login(request):
    req_body = json.loads(request.body.decode('utf-8'))
    email = req_body.get('email')
    password = req_body.get('password')
    valid = check_login(email, password)
    if valid:
        # request.session['user_id'] = valid[0]
        if valid[5] is None:
            return HttpResponse(all_flights())
        if valid[5] == 'airlineEmp':
            return HttpResponse(all_flights(airline=valid[6]))
        return HttpResponse(all_gate_records())
    return HttpResponse(json.dumps({'msg': 'invalid credentials'}))


def all_flights(airline=None):
    flights = all_flights_in_db(airline)
    f_list = []
    for flight in flights:
        f_list.append({
            'flight_id': flight[0],
            'aircraft_id': flight[1],
            'company_airline': flight[2],
            'type_of_flight': flight[3],
            'terminal': flight[4],
            'time_at_gate': flight[5],
            'destination': flight[6],
            'gate_id': flight[8]
        })
    return f_list


def edit_flight_timings(request):
    req_body = json.loads(request.body.decode('utf-8'))
    flight_id = req_body.get('flight_id')
    time = req_body.get('time')
    updated = update_flight_time(flight_id, time)
    if updated:
        return HttpResponse('updated')


def all_gate_records():
    setup_gate()
    data = get_all_gates_information()
    f_list = []
    for gate in data:
        f_list.append({
            'flight_id': gate[0],
            'gate_number': gate[1]
        })
    return f_list


def setup_gate():
    free_gate()
    gates, flights = setup_gates()
    leng = min(len(gates), len(flights))
    for i in range(0, leng):
        insert_flights_gates(gates[i][0], flights[i][0])
    return 0

