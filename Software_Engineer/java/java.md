

## overloading vs overriding

overloading: same method but different parapmeter in the same class

overriding : same method signature in super class and child class

## collection framwork
ArrayList
Vector
LinkedList
HashMap

ArrayList is not synchroized, but Vector is synchroized
LinkedList can act like list and queue

ArrayList:
add()
remove()
hasSize()

Vector:
add()
remove()
size()

LinkedList:
add()



## interms of the inheritance, what is the effect of keeping the constructive private?

declaring a constructor private on class. A means that you can only access the private constructor if you could also access a private methods. who, other than A, can access A private methods and constructor ? a inner classes can. additionally, if A is an inner class of Q, thne Q's other inner class can.


## in Java, does the finally block get executed if we insert a return statement inside the try block of a try-catch-finally?

Yes, it will get executed the finaaly block get executed when the ty block exists. even when we attempt to exist within the try block (via a return statement, a continue statement, a break statement or any other exception), then finally block will be executed.

note that there are some cases in which the finally block will not get executed, such as following:
1. if the virutal machine exists during try/catch block execution
2. if the thread which is executing during the try/catch block get killed.

## what is the difference between final, finally and finalize ?


final class , any attempt to inherit from a final class will cause a compiler error
final methods, methods marked as final cannot be overridden
final variables, cann't be reassigned
final reference, cann't be reassigned

finally is the block in exception handling 

finalize is the method of object class. it is the method is Java which is used to perform clean up processing just before object is garbage collected. 

the automatic garbage collector calls the finalize() method just before actually destroying the object. A class can therfore override the finalize() method from the object class in order to define custom behavior during garbage collections.


``` java
public class FinalizeExample {    
     public static void main(String[] args)     
    {     
        FinalizeExample obj = new FinalizeExample();        
        // printing the hashcode   
        System.out.println("Hashcode is: " + obj.hashCode());           
        obj = null;    
        // calling the garbage collector using gc()   
        System.gc();     
        System.out.println("End of the garbage collection");     
    }     
   // defining the finalize method   
    protected void finalize()     
    {     
        System.out.println("Called the finalize() method");     
    }     
}    

``` shell

output:
```
java FinalizeExample
Hashcode is: 746292446
End of the garbage collection
Called the finalize() method
```


## templates in C++ vs Generics in Java

the implementation of Java generics is rooted in an idea of " type erasure". this technique eliminates the parameterized types when source code is translated to the java virtual machine(JVM)

``` java
List<Integer> list = new LinkedList();
list.add(new Integer(1));
Integer i = list.iterator().next();
```
the use of java generics didn't really change much about our capabilities; it just made things a bit prettier. for this reason, Java generics are sometimes caleed " syntactic sugar"

1. C++ templates can use primitive types, like int. Java cannot and must instead use Integer.
2. in Java, you can restrict the template's type parameters to be of a certain type. for instance, you might use generics to implement a cardDeck and specify that the type parameter must extend from CardGame.
3. In C++ , the type parameter can be instantiated, whereas Java does not support this.
4. In Java, the type parameter cannot be used for static methods and variables, since these would be shared between MyClass<Foo> and MyClass<Bar>. In C++, these classes are different, os the type parameter can be used for static methods and variables.
    
## TreeMap, HashMap, LinkedHashMap
     
HashMap O(1) lookup and insertion. the order of the key is arbitrary
TreeMap O(N) lookup and insertion. sorted order
LinkedHashMap O(1) lookup and insertion. key are ordered by their insertion order
     
when might you need ordering in real life ?

suppose you were creating a mapping of names to Person Object. you might want to periodically output the people in alphabetical order by name. A treeMap let you do this.
A linkedHashMap is useful whenever you need the ordering of keys to match the ordering of insertion. this might be useful in a caching situation. when you want to delete the oldest item.
Generally, use HashMap. it is typically faster and require less overhead.

## object reflection
     
1. getting information about the methods and fields present inside the class at runtime.
2. creating a new instance of class
3. Get and set the object fields directly by getting field reference, regardless of what the access modifier is.

Why is Object Reflection Useful?
1. it can help you observer or manipulate the runtime behavior of applications
2. It can help you debug or test programs, as you habe direct access to methods, constructors and fields

     
## Lambda Expressions
     
     
 
     
What is Java? Explain its features and benefits.
     
     
     
What is the difference between JDK, JRE, and JVM?
What is OOP? Explain the four fundamental concepts of OOP.
What is a class and object in Java?
What is inheritance? Explain the types of inheritance in Java.
What is Polymorphism? Explain the types of Polymorphism in Java.
What is an interface in Java?
What is an abstract class in Java?
What is the difference between an abstract class and an interface?
What is Exception Handling in Java? Explain different types of exceptions in Java.
What are the access modifiers in Java?
What is the difference between final, finally, and finalize in Java?
What is the difference between an ArrayList and a LinkedList in Java?
What is a HashMap in Java?
What is a Thread in Java? Explain the life cycle of a Thread.
What is synchronization in Java? How can we achieve synchronization in Java?
What is the difference between wait() and sleep() methods in Java?
What is the difference between a Stack and a Queue in Java?
What is JDBC in Java? Explain its components.
What is the difference between inner and outer join in SQL?

     
     
 Java 17 new feature
     
     Sealed Classes in java 17
     
     sealed classes are a new feature introduced in Java 15 and further enhanced in Java 17 that allows developers to restrict the subtypes of a class, providing better control over class hierarchies
     
     
     pattern matching in java 17
     
     
     
     
1.	abstract	Specifies that a class or method will be implemented later, in a subclass 
2.	assert	Assert describes a predicate placed in a java program to indicate that the developer thinks that the predicate is always true at that place.
3. 	boolean	A data type that can hold True and False values only 
4.	break	A control statement for breaking out of loops.
5.	byte	A data type that can hold 8-bit data values 
6.	case	Used in switch statements to mark blocks of text
7.	catch	Catches exceptions generated by try statements
8.	char 	A data type that can hold unsigned 16-bit Unicode characters
9.	class	Declares a new class
10.	continue	Sends control back outside a loop 
11.	default	Specifies the default block of code in a switch statement
12.	do	Starts a do-while loop
13.	double	A data type that can hold 64-bit floating-point numbers
14.	else	Indicates alternative branches in an if statement 
15.	enum	A Java keyword is used to declare an enumerated type. Enumerations extend the base class.
16.	extends	Indicates that a class is derived from another class or interface 
17.	final	Indicates that a variable holds a constant value or that a method will not be overridden
18.	finally	Indicates a block of code in a try-catch structure that will always be executed
19.	float	A data type that holds a 32-bit floating-point number 
20.	for	Used to start a for loop
21.	if	Tests a true/false expression and branches accordingly
22.	implements	Specifies that a class implements an interface 
23.	import 	References other classes
24.	instanceof	Indicates whether an object is an instance of a specific class or implements an interface 
25.	int	A data type that can hold a 32-bit signed integer 
26.	interface	Declares an interface
27.	long	A data type that holds a 64-bit integer
28.	native	Specifies that a method is implemented with native (platform-specific) code 
29.	new	Creates new objects 
30.	null	This indicates that a reference does not refer to anything 
31.	package	Declares a Java package
32.	private	An access specifier indicating that a method or variable may be accessed only in the class it’s declared in
33.	protected	An access specifier indicating that a method or variable may only be accessed in the class it’s declared in (or a subclass of the class it’s declared in or other classes in the same package)
34.	public	An access specifier used for classes, interfaces, methods, and variables indicating that an item is accessible throughout the application (or where the class that defines it is accessible)
35.	return	Sends control and possibly a return value back from a called method 
36.	short	A data type that can hold a 16-bit integer 
37	static	Indicates that a variable or method is a class method (rather than being limited to one particular object)
38.	strictfp	A Java keyword is used to restrict the precision and rounding of floating-point calculations to ensure portability.
39.	super	Refers to a class’s base class (used in a method or class constructor) 
40.	switch	A statement that executes code based on a test value 
41.	synchronized	Specifies critical sections or methods in multithreaded code
42.	this	Refers to the current object in a method or constructor 
43.	throw 	Creates an exception 
44.	throws	Indicates what exceptions may be thrown by a method 
45.	transient	Specifies that a variable is not part of an object’s persistent state
46.	try	Starts a block of code that will be tested for exceptions 
47.	void	Specifies that a method does not have a return value
48.	volatile	This indicates that a variable may change asynchronously
49.	while	Starts a while loop


     

