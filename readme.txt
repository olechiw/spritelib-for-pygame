#**************************************
#Please Note:
#The default sprite size is set to (20, 20)
#You can change this on lines 66, 139, 236 etc. (in the __init__ functions)
#**************************************
#Usage:
#ignore sprite_base!!! ignore sprite_base!!! ignore sprite_base!!! ignore sprite_base!!! (its just your basic sprite class in pygame)
#    from pygame import spritelibs
#    self.my_sprite = spritelibs.updown('foo.image', (x, y))
#    self.my_sprite.group.draw()
#    def update(self):
#        self.my_sprite.update_func(self.my_window, self.other_groups)
#the above code will make a sprite that, whenever update is called,
#will move left, then if there is a collision move right, then
#keep moving right till there is a collision, then move left until
#there is a collision, etc. the static_base class can be used
#for your own animations with different functions then just
#updating.
#**************************************
#About:
#This is a library to extend pygame for those who dont want
#to write their own
##BY:PIANIST1119