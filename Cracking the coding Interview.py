#1. Arrays and Strings

#Implement an algorithm to determine if a string has all unique charactersself.
#What if you cannot use additional data structures?

def all_unique(string):
  list = []
  for i in range(0,len(string)-1):
    if string[i] not in list:
      list.append(string[i])
    else:
      return "This string does not include all unique characters"
      break
  return "This string contains all unique characters"

#Without additional data structures

def all_unique(string):
  for i in range(0,len(string)-1):
    if string[i] not in string[0:i]:
      pass
    else:
      return "This string does not include all unique characters"
      break
  return "This string contains all unique characters"

  #Given two strings, write a method to decide if one is a permutation of the otherself.

def permutation_check(str1, str2):
    dict = {}
    if len(str1) != len(str2):
        return False
    for i in range(0,len(str1)-1):
        if str1[i] in str2[0:]:
            if str[i] not in dict:
                dict[str[i]] = 1
            else:
                dict[str[i]] += 1
    for key in dict:
        if key in dict > 1:
            return False
        else:
            return True

#Write a method to replace all spaces in a string with "%20". You may assume
#that the string has sufficient space at the end to hold the additional lettersself.

def replace20(string):
    space_count = 0
    for i in range(0, len(string)-1):
        if string[i] == " ":
            space_count +=1
            string[i+3:len(string)-1 + space_count*2] = string[i+1:]
            string[i] = "%20"
    return string

#Given a string, write a function to check if it is a palindrome
def palindrome(string):
    string2 = string[-1::]
    for i in range(0, len(string)):
        if string[0] == string2[0]:
            pass
        else:
            return False
    return True

#Assume a method isSubstring that will check if a string is a rotation of another string2
#Use only one call to isSubstring to check if str2 is a rotation of str1

def isSubstring(str1, str2):
    if len(str1) == len(str2) and len(str1)>0:
        str1str1 = str1 + str1
        isSubstring(str1str1, str2)


# #Write code to remove duplicates from an unsorted linked list
# '''class Node(object):
#    def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class LinkedList(object):
#    def __init__(self, data):
#         self.size = 0
#         self.head = None'''

    def remove_duplicates():
        list = []
        while self.head != None:
            if self.head.data not in list:
                list.append(self.head.data)
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
            self.head = self.head.next


#Implement an algorithm to find the kthto last element of a singly linked listself.

    def kth_last(k):
        i = 1
        if k > self.size+1:
            return "That numbered element does not exist."
        while self.head.next != None:
            self.head = self.next
        while i < k:
            self.head = self.head.prev
            i += 1
        return self.head.data

#Implement an algorithm to delete the middle node in a linked listself

    def delete_middle():
        node1 = self.head
        node2 = self.head
        while node2.next.next != None:
            node2 = node2.next.next
            node1 = node1.next
        if node2.next.next == None:
            node1.next = node1.next.next



#SetofStacks should be composed of several stacks and should create a new stack once the
#previous one exceeds capacity. Pop() and Push() should return values as if it were a single stackself.

class Stack(object):
    def __init__(self, capacity):
            self.stack = []
            self.lastStack = None
            self.nextStack = None
            self.capacity = capacity

class SetofStacks(object):
    def __init__(self,capacity):
            self.lastStack = None
            self.nextStack = None
            self.size = 0
    def getLastStack():
        self.stack = self.lastStack
        if self.size >= 3:
            self.lastStack = self.lastStack.lastStack
            self.size -=1
        else:
            self.lastStack = None
            self.size -= 1

    def push(self,value):
        self.value = value
        if len(self.stack) < self.capacity:
            self.stack.append(self.value)
        else:
            self.lastStack = self.stack
            self.stack = Stack(self.capacity)
            self.stack.stack.append(self.value)
    def pop():
        if len(self.stack) == 0:
            self.getLastStack()
            self.stack.pop()
        else:
            self.stack.pop()
