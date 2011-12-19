tri_set = set([i*(i+1)/2 for i in range(285, 100000)])
pen_set = set([i*(3*i-1)/2 for i in range(165, 100000)])
hex_set = set([i*(2*i-1) for i in range(143, 100000)])
print tri_set & pen_set & hex_set

    