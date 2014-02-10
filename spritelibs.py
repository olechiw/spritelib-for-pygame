#**************************************
#Please Note:
#The default sprite size is set to (20, 20)
#You can change this on lines 66, 139, 236 etc. (in the __init__ functions)
#**************************************
#Usage:
#ignore: sprite_base
#To use this library simply set your variable like this:
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
import pygame, os
class sprite_base(pygame.sprite.Sprite):
        def __init__(self, image_file, location, size):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image_file)
            self.image_name = image_file
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
            self.image = pygame.transform.scale(self.image, size)
            self.pos = location
class updown():
    def move_down(self, sprite, group, groups, surface):
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0], sprite.absolute_pos[1]+20), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                group.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_up(self, sprite, group, groups, surface):
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0], sprite.absolute_pos[1]-20), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def __init__(self, image, location):
        self.sprite = sprite_base(image, location, ((20, 20)))
        self.group = pygame.sprite.Group(self.sprite)
        self.default = False
    def updatefunc(self, surface, groups):
        if not self.default:
            returned = self.move_up(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = True
        if self.default:
            returned = self.move_down(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = False
        return [surface, groups]
class downup():
    def move_down(self, sprite, group, groups, surface):
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0], sprite.absolute_pos[1]+20), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                group.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_up(self, sprite, group, groups, surface):
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0], sprite.absolute_pos[1]-20), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def __init__(self, image, location):
        self.sprite = sprite_base(image, location, ((20, 20)))
        self.group = pygame.sprite.Group(self.sprite)
        self.default = False
    def updatefunc(self, surface, groups):
        if not self.default:
            returned = self.move_down(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = True
        if self.default:
            returned = self.move_up(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = False
        return [surface, groups]
class leftright():
    def move_right(self, sprite, group, groups, surface):
            image = os.path.splitext(sprite.image_name)[0]
            image = str(image)
            images = []
            for i in image:
                if i != '_':
                    images.append(i)
                else:
                    break
            image = ''
            for i in images:
                image += i
            image += "_lookr.png"
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0]-20, sprite.absolute_pos[1]), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_left(self, sprite, group, groups, surface):
            image = os.path.splitext(sprite.image_name)[0]
            image = str(image)
            images = []
            for i in image:
                if i != '_':
                    images.append(i)
                else:
                    break
            image = ''
            for i in images:
                image += i
            image += "_lookr.png"
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0]+20, sprite.absolute_pos[1]), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def __init__(self, image, location):
        self.sprite = sprite_base(image, location, ((20, 20)))
        self.group = pygame.sprite.Group(self.sprite)
        self.default = False
    def updatefunc(self, surface, groups):
        if not self.default:
            returned = self.move_left(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = True
        if self.default:
            returned = self.move_right(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = False
        return [surface, groups]
class rightleft():
    def move_right(self, sprite, group, groups, surface):
            image = os.path.splitext(sprite.image_name)[0]
            image = str(image)
            images = []
            for i in image:
                if i != '_':
                    images.append(i)
                else:
                    break
            image = ''
            for i in images:
                image += i
            image += "_lookr.png"
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0]-20, sprite.absolute_pos[1]), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_left(self, sprite, group, groups, surface):
            image = os.path.splitext(sprite.image_name)[0]
            image = str(image)
            images = []
            for i in image:
                if i != '_':
                    images.append(i)
                else:
                    break
            image = ''
            for i in images:
                image += i
            image += "_lookr.png"
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0]+20, sprite.absolute_pos[1]), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def __init__(self, image, location):
        self.sprite = sprite_base(image, location, ((20, 20)))
        self.group = pygame.sprite.Group(self.sprite)
        self.default = False
    def updatefunc(self, surface, groups):
        if not self.default:
            returned = self.move_right(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = True
        if self.default:
            returned = self.move_left(self.sprite, self.group, groups, surface)
            self.sprite = returned[0]
            self.group = returned[1]
            collided = returned[2]
            groups = returned[3]
            surface = returned[4]
            if collided:
                self.default = False
        return [surface, groups]
class static_base():
    def move_down(self, sprite, group, groups, surface):
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0], sprite.absolute_pos[1]+20), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                group.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_up(self, sprite, group, groups, surface):
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0], sprite.absolute_pos[1]-20), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_right(self, sprite, group, groups, surface):
            image = os.path.splitext(sprite.image_name)[0]
            image = str(image)
            images = []
            for i in image:
                if i != '_':
                    images.append(i)
                else:
                    break
            image = ''
            for i in images:
                image += i
            image += "_lookr.png"
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0]-20, sprite.absolute_pos[1]), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def move_left(self, sprite, group, groups, surface):
            image = os.path.splitext(sprite.image_name)[0]
            image = str(image)
            images = []
            for i in image:
                if i != '_':
                    images.append(i)
                else:
                    break
            image = ''
            for i in images:
                image += i
            image += "_lookr.png"
            sprite2 = sprite_base(sprite.image_name, (sprite.absolute_pos[0]+20, sprite.absolute_pos[1]), ((20, 20)))
            sprite2s = pygame.sprite.Group(sprite2)
            sprite2s.draw(surface)
            collided = False
            for i in groups:
                collide_sprite = pygame.sprite.groupcollide(sprite2s, i, False, False)
                for x in collide_sprite:
                    collided = True
            if not collided:
                groups.remove(sprite)
                del groups[groups.index(group)]
                pygame.draw.rect(surface, [0, 0, 0], [sprite.absolute_pos[0], sprite.absolute_pos[1], 20, 20], 0)
                groups.append(sprite2s)
                del sprite, sprite2s
                group.add(sprite2)
                pygame.display.flip()
                return [sprite2, group, collided, groups, surface]
            else:
                pygame.draw.rect(surface, [0, 0, 0], [sprite2.absolute_pos[0], sprite2.absolute_pos[1], 20, 20], 0)
                del sprite2s, sprite2
                for i in groups:
                    i.draw(surface)
                return [sprite, group, collided, groups, surface]
    def __init__(self, image, location):
        self.sprite = sprite_base(image, location, ((20, 20)))
        self.group = pygame.sprite.Group(self.sprite)
        self.default = False
    def updatefunc(self, foo1, foo2):
        pass
    def right(self):
        pass
    def left(self):
        pass
    def up(self):
        pass
    def down(self):
        pass