from ps3b import SimpleVirus, Patient

patient = Patient([SimpleVirus(0.5, 0.1)], 10)

for _ in range(50):
    print(patient.update())
