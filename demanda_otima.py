import csv
import statistics
import math
import pprint

def calculaValor(v, contratado, T):
	final = {
		"multa": [],
		"mensal": []
	}

	for elemv in v:
		if elemv <= contratado:
			final["mensal"].append(round(contratado*T, ndigits=2))
			final["multa"].append(0)
		elif elemv <= 1.05*contratado:
			final["mensal"].append(round(elemv*T, ndigits=2))
			final["multa"].append(0)
		else:
			final["mensal"].append(round(T*(contratado + (elemv - contratado)*2), ndigits=2))
			final["multa"].append(round(T*(elemv - contratado)*2, ndigits=2))

	final["anual"] = sum(final["mensal"])
	final["multa_anual"] = round(sum(final["multa"]), ndigits=2)

	return final


v = []

with open('in.txt', 'r') as infile:
	for i in range(0,12):
		v.append(float(infile.readline()))

	T = float(infile.readline())

	print("Taxa: "+str(T))
	print("Medidas mensais: "+str(v))

	maximo = max(v)
	minimo = min(v)
	media = math.ceil(statistics.mean(v))

	calculo_maximo = calculaValor(v, maximo, T)
	calculo_minimo = calculaValor(v, minimo, T)
	calculo_media = calculaValor(v, media, T)

	print("MAXIMO: " + str(maximo))
	pprint.pprint(calculo_maximo)
	print("---------------------------------")
	print("MINIMO: " + str(minimo))
	pprint.pprint(calculo_minimo)
	print("---------------------------------")
	print("MEDIA: " + str(media))
	pprint.pprint(calculo_media)
    
	candidate = min(v)
	end = max(v)
	opt = calculaValor(v, candidate, T)
	cand_opt = candidate
	while (candidate <= end):
			localtest = calculaValor(v, candidate, T)
			if(localtest["anual"] < opt["anual"]):
					opt = localtest
					cand_opt = candidate
			candidate += 1

	print("---------------------------------")
	print("OTIMO: " + str(round(cand_opt, ndigits=2)))
	pprint.pprint(opt)

	with open('out.txt', 'w') as outfile:
		outfile.write("Max: "+str(maximo)+"\n")
		outfile.write("Anual: "+str(calculo_maximo["anual"])+"\n")
		outfile.write("Mensal: "+str(calculo_maximo["mensal"])[1:-1]+"\n")
		outfile.write("Multa: "+str(calculo_maximo["multa_anual"])+"\n")
		outfile.write("Multa Mensal: "+str(calculo_maximo["multa"])[1:-1]+"\n")
		outfile.write("\n")
		outfile.write("Min: "+str(minimo)+"\n")
		outfile.write("Anual: "+str(calculo_minimo["anual"])+"\n")
		outfile.write("Mensal: "+str(calculo_minimo["mensal"])[1:-1]+"\n")
		outfile.write("Multa: "+str(calculo_minimo["multa_anual"])+"\n")
		outfile.write("Multa Mensal: "+str(calculo_minimo["multa"])[1:-1]+"\n")
		outfile.write("\n")
		outfile.write("Media: "+str(media)+"\n")
		outfile.write("Anual: "+str(calculo_media["anual"])+"\n")
		outfile.write("Mensal: "+str(calculo_media["mensal"])[1:-1]+"\n")
		outfile.write("Multa: "+str(calculo_media["multa_anual"])+"\n")
		outfile.write("Multa Mensal: "+str(calculo_media["multa"])[1:-1]+"\n")
		outfile.write("\n")
		outfile.write("Otima: "+str(cand_opt)+"\n")
		outfile.write("Anual: "+str(opt["anual"])+"\n")
		outfile.write("Mensal: "+str(opt["mensal"])[1:-1]+"\n")
		outfile.write("Multa: "+str(opt["multa_anual"])+"\n")
		outfile.write("Multa Mensal: "+str(opt["multa"])[1:-1]+"\n")
		outfile.write("\n")