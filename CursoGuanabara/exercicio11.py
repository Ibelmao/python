larg = float(input('Qual a largura da parede :'))
alt = float(input('Altura da parede: '))
area = larg* alt
print('Sua parede tem a dimensaoão de {} x {} e sua área é de {}m2.'.format(larg, alt, area))
tenta = area / 2 
print('Para pintar essa parece, vc precisará de {} L de tinta '.format(tenta))
