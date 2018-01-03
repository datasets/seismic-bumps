from urllib.request import urlopen

with open("data/seismic-bumps.csv", "w") as bumps_file:
    bumps_file.write("seismic,seismoacoustic,shift,genergy,gpuls,gdenergy,gdpuls,ghazard,"
                     "nbumps,nbumps2,nbumps3,nbumps4,nbumps5,nbumps6,nbumps7,nbumps89,energy,maxenergy,class\n")
    data_found = False
    for line in urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/00266/seismic-bumps.arff"):
        decodedLine = line.decode('UTF-8')
        print(decodedLine)

        if data_found:
            bumps_file.write(decodedLine.strip() + '\n')

        if decodedLine.strip() == '@data':
            data_found = True

    bumps_file.close()
