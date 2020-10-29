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
			final["mensal"].append(round(T*(contratado + (elemv - contratado)*3), ndigits=2))
			final["multa"].append(round(T*(elemv - contratado)*3, ndigits=2))

	final["anual"] = round(sum(final["mensal"]), ndigits=2)
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
		outfile.write("Max: "+format(maximo, ',.2f')+"\n")
		outfile.write("Anual: "+format(calculo_maximo["anual"], ',.2f')+"\n")
		outfile.write("Mensal: "+", ".join([format(value, ',.2f') for value in calculo_maximo["mensal"]])+"\n")
		outfile.write("Multa: "+format(calculo_maximo["multa_anual"], ',.2f')+"\n")
		outfile.write("Multa Mensal: "+", ".join([format(value, ',.2f') for value in calculo_maximo["multa"]])+"\n")
		outfile.write("\n")
		outfile.write("Min: "+format(minimo, ',.2f')+"\n")
		outfile.write("Anual: "+format(calculo_minimo["anual"], ',.2f')+"\n")
		outfile.write("Mensal: "+", ".join([format(value, ',.2f') for value in calculo_minimo["mensal"]])+"\n")
		outfile.write("Multa: "+format(calculo_minimo["multa_anual"], ',.2f')+"\n")
		outfile.write("Multa Mensal: "+", ".join([format(value, ',.2f') for value in calculo_minimo["multa"]])+"\n")
		outfile.write("\n")
		outfile.write("Media: "+format(media, ',.2f')+"\n")
		outfile.write("Anual: "+format(calculo_media["anual"], ',.2f')+"\n")
		outfile.write("Mensal: "+", ".join([format(value, ',.2f') for value in calculo_media["mensal"]])+"\n")
		outfile.write("Multa: "+format(calculo_media["multa_anual"], ',.2f')+"\n")
		outfile.write("Multa Mensal: "+", ".join([format(value, ',.2f') for value in calculo_media["multa"]])+"\n")
		outfile.write("\n")
		outfile.write("Otima: "+format(cand_opt, ',.2f')+"\n")
		outfile.write("Anual: "+format(opt["anual"], ',.2f')+"\n")
		outfile.write("Mensal: "+", ".join([format(value, ',.2f') for value in opt["mensal"]])+"\n")
		outfile.write("Multa: "+format(opt["multa_anual"], ',.2f')+"\n")
		outfile.write("Multa Mensal: "+", ".join([format(value, ',.2f') for value in opt["multa"]])+"\n")
		outfile.write("\n")