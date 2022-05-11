//Semicolons are optional in kotlin
// Main Class / This is where the program starts excecuting 
fun main() {

    // Variables
        // var mutable and val is a constant variable (immutable)
        var mutableInt = 99
        val immutableInt = 99

        // Explicit type
        var hello : String = "hi"
        //Explicit type with null safety
        var willBeNull : String? = null
    
    // Collections
        // Arrays
        val numArray = arrayOf(1, 2, 3)

        // List
        val numList = listOf(1, 2, 3)
        val mutableNumList = mutableListOf(1, 2, 3)
        
        // Map + Immutable to mutable
        val immutableMap = mapOf("Jack" to 11, "Queen" to 12, "King" to 13)
        val mutableMap = immutableMap.toMutableMap()

        // Built-in collection methods
        // val evenNumbers = numList.filter { it % 2 == 0 }
        // val containsEven = numList.any { it % 2 == 0 }
        // val containsNoEvens = numList.none { it % 2 == 0 }
        // val containsNoEvens = numList.all { it % 2 == 1 }
        // val firstEvenNumber: Int = numList.first { it % 2 == 0 }
        // val firstEvenOrNull: Int? = numList.firstOrNull { it % 2 == 0 }
    
    
    // Conditional Statements
        // If else
        if (someBoolean) {
            doThing()
        } else {
            doOtherThing()
        }

        // When statement
        when (direction) {
            NORTH -> {
                print("North")
            }
            SOUTH -> print("South")
            EAST, WEST -> print("East or West")
            "N/A" -> print("Unavailable")
            else -> print("Invalid Direction")
        }
        

    // Loops
        // For
        for (item in myList) {
            print(item)
        }
        
        // For each
        myList.forEach {
            print(it)
        }
        
        // For each with index
        myList.forEachIndexed { index, item -> 
            print("Item at $index is: $item")
        }

        // While
        while (x > 0) {
            x--
        }
        
        do {
            x--
        } while (x > 0)

    // Functions
    fun doubleTheNumber(x: Int) = x * 2
    val lambdaFun: (Int) -> Int = {num -> doubleTheNumber(num)}

    fun printName() {
        print("Adam")
    }
    
    fun printName(person: Human) {
        print(person.name)   
    }
    
    fun getGreeting(person: Human): String {
        return person.hey
    }

    //Classes & Objects
    class Human {
        // attributes
        val name = "Vilius"

        // methods
        fun hey() {
            println("hello")
        }
    }

    // Exceptions
        try {
            // some code
        } catch (e: SomeException) {
            // handler
        } finally {
            // optional finally block
        }
        // or 
        throw Exception("Hi There!")

    
}