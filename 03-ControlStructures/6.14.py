influencer = input('Enter influencer nickname: ')
facebook = False
x = False
ig = False
i_fb = input(f'Does {influencer} have facebook?(yes/no): ')
if i_fb == 'yes':
    facebook = True
i_x = input(f'Does {influencer} have x?(yes/no): ')
if i_x == 'yes':
    x = True
i_ig = input(f'Does {influencer} have ig?(yes/no): ')
if i_ig == 'yes':
    ig = True
if facebook + ig + x >= 2:
    print(f'{influencer} is a good influencer')
else:
    print(f'{influencer} is not a good influencer')