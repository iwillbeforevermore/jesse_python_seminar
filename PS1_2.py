from visual import*
alice = sphere(pos = vector(-1,0,0), radius = .25, color = color.red)
bob = sphere(pos = vector(1,0,0), radius = .25, color = color.yellow)
carl = sphere(pos = vector(0,1,0), radius = .25, color = color.blue)

arrow(pos = alice.pos, axis = bob.pos-alice.pos, color = color.orange)
arrow(pos = bob.pos, axis = carl.pos-bob.pos, color = color.orange)
arrow(pos = carl.pos, axis = alice.pos-carl.pos, color = color.orange)
