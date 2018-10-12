from django.http import HttpResponse
from django.shortcuts import render
import json

file = open("json_data.json", "r", encoding="utf8")
text = file.read()
file.close()
data = json.loads(text)
col_administration_unints = len(data["units"]["administration"])
col_mega_fac = len(data["units"]["education"])
col_fac = 0
for mega_fac in data["units"]["education"]:
    col_fac += len(mega_fac["faculties"])
col_cathedr = 0
education_programs = []

groups = []

for mega_fac in data["units"]["education"]:
    for fac in mega_fac["faculties"]:
        col_cathedr += len(fac["cathedr"])
        for cathedra in fac["cathedr"]:
            for education_program in cathedra["education_programs"]:
                education_programs.append(education_program)
                for year in education_program["year"]:
                    groups.extend(education_program["year"][year])
col_education_units = col_fac + col_cathedr + col_mega_fac

def index(request):
    return HttpResponse("Hello, world!")


def indexRender(request):
    return render(request, 'index.html', {})


def universityInfo(request):
    return render(request, 'universityInfo.html', {
        "json": data,
        "col_fac": col_fac,
        "col_cathedr": col_cathedr,
        "col_mega_fac": col_mega_fac,
        "col_administration_unints": col_administration_unints,
        "col_education_units": col_education_units
    })


def disciplineInfo(request):
    return render(request, 'disciplineInfo.html', {
        "ed_prog_count": len(education_programs),
        "ed_prog": education_programs
    })


def groupsInfo(request):
    return render(request, 'groupsInfo.html', {
        "groups": groups
    })
