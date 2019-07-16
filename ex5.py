my_name = 'Mason E. Gil'
my_age = 20
my_height = 12 * 6 + 4
my_weight = 190
my_eyes = 'Brown'
my_teeth = 'Glistening'
my_hair = "Maroon"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "Hes's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
