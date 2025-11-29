"""
 Python Data Types Demonstration for Mathematics Teachers
 Answear to Day 1 Exercise 1 Python basics and mathematical applications:
       1. Define variables for different data types (integers, floats, strings)
       2. Create lists to store multiple values like test scores
 Post reflection: 
 I should make it less abstract and more practical for teachers,
 focusing on real-world applications in education. 

 TODO: 
 [] Improve examples related to educational data analysis
 [] (Pros and Crontra)Include comments explaining each data type's relevance to concrete applications.
 [x] Improve the print formatting for better readability.
  - [] Add Help descriptions for each method and operation.
  - [] Capture the concepts in outputs to make a (dinamic/IA-Powered/Data-Powered) dictionary for future reference.
 [X] Add interactive input prompts for users to experiment with data types in real-time educational scenarios.
 [] Integrate simple visualizations to graphically represent data operations, like print in different for the data type and phrases in code.
"""
import types
import matplotlib.pyplot as plt
import sys
import dis
import inspect
import ast
import gc
from collections import defaultdict

def press_enter_to_continue(message="Press Enter to continue..."):
    """Interactive pacing control to prevent information overload."""
    try:
        input(f"\n🔸 {message}")
    except KeyboardInterrupt:
        print("\n👋 Session interrupted by user.")
        sys.exit(0)

def show_learning_level(level_num, title, description):
    """Display learning level header with clear formatting."""
    level_symbols = ["🌟", "🔬", "⚛️", "🧬"]
    print(f"\n{'='*80}")
    print(f"{level_symbols[level_num-1]} LEVEL {level_num}: {title.upper()}")
    print(f"{'='*80}")
    print(f"{description}")
    print(f"{'='*80}")

def demonstrate_with_introspection(obj, show_bytecode=False):
    """Enhanced demonstration combining surface and deep introspection."""
    print(f"\n🔍 ANALYZING: {obj} (type: {type(obj).__name__})")

    # Level 1: Surface Level - Basic Concepts
    show_learning_level(1, "Surface Level", "Understanding the basic nature and documentation of data types")
    press_enter_to_continue("Ready to explore the surface level?")

    print(f"    📖 What is {type(obj).__name__}?")
    doc = type(obj).__doc__
    if doc:
        doc_summary = doc.split('.')[0] if '.' in doc else doc[:100]
        print(f"    📚 Official Documentation: {doc_summary}...")
    else:
        print(f"    📚 No official documentation available.")

    print(f"    🔍 Type: {type(obj)}")
    print(f"    📝 String representation: {str(obj)}")
    print(f"    💻 Repr representation: {repr(obj)}")

    # Level 2: Intermediate Level - Practical Applications
    show_learning_level(2, "Intermediate Level", "How data types behave in practical educational scenarios")
    press_enter_to_continue("Ready to see practical applications?")

    print(f"    🏫 Educational Context: {obj}")
    print(f"    📊 Memory footprint: {sys.getsizeof(obj)} bytes")
    print(f"    🆔 Unique identity: {id(obj)}")

    try:
        h = hash(obj)
        print(f"    🔒 Hash value: {h} (can be used as dict key)")
    except TypeError:
        print(f"    🚫 Not hashable (mutable type)")

    # Level 3: Deep Level - Python's Internal Processing
    show_learning_level(3, "Deep Level", "How Python processes and manages data internally")
    press_enter_to_continue("Ready to dive deep into Python's internals?")

    print(f"    🏗️ Class Hierarchy:")
    for i, cls in enumerate(type(obj).__mro__):
        print(f"      {i+1}. {cls.__name__} ({cls.__module__})")

    print(f"    📊 Object attributes: {len(dir(obj))} total")
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr, None))]
    print(f"    ⚙️ Callable methods: {len(methods)}")

    # Show bytecode if requested
    if show_bytecode and callable(obj):
        print(f"    📋 Bytecode disassembly:")
        try:
            dis.dis(obj)
        except:
            print(f"      Could not disassemble {obj}")

    # Level 4: Core Level - System Integration
    show_learning_level(4, "Core Level", "How Python integrates with the underlying system and C runtime")
    press_enter_to_continue("Ready to explore the core system level?")

    print(f"    🔄 CPython Object Model:")
    print(f"      • C Structure: {type(obj).__name__} objects are C structs")
    print(f"      • Memory Management: Handled by Python's garbage collector")
    print(f"      • Reference Counting: {sys.getrefcount(obj)} references to this object")

    # Show garbage collector info
    gc_info = gc.get_stats()
    print(f"    🗑️ Garbage Collection: {len(gc_info)} generations active")

    print(f"    🎯 Key Insight: Every Python object is a C structure with Python-level behavior!")
    press_enter_to_continue("Reflect on what you've learned about this data type")
import dis
import inspect
import ast
import gc
from collections import defaultdict

def demonstrate_universal_methods(obj):
    """Demonstrates universal methods on an object with deep introspection."""
    print(f"    🔍 the type({obj}) is {type(obj)}")
    print(f"      📖 Help: \n        Returns the type of the object as a type object. This is useful for understanding what kind of data you're working with and for type checking in your programs.\n")
    
    # Deep introspection section
    obj_type = type(obj)
    print(f"    🧬 DEEP PYTHON INTROSPECTION:")
    
    # Documentation
    if hasattr(obj_type, '__doc__') and obj_type.__doc__:
        doc = obj_type.__doc__.strip().split('\n')[0] if obj_type.__doc__ else "No documentation available"
        print(f"    📚 __doc__: {doc}")
        print(f"      📖 Help: \n        The docstring of the type class. Provides official documentation about what this type represents and how it behaves.\n")
    
    # Class hierarchy
    print(f"    🏗️  __class__: {obj_type.__class__}")
    print(f"      📖 Help: \n        The metaclass of this type. Every type in Python is an instance of a metaclass, usually 'type'.\n")
    
    print(f"    📦 __module__: {getattr(obj_type, '__module__', 'built-in')}")
    print(f"      📖 Help: \n        The module where this type is defined. Built-in types have no specific module.\n")
    
    # Method Resolution Order
    if hasattr(obj_type, '__mro__'):
        mro_names = [cls.__name__ for cls in obj_type.__mro__]
        print(f"    🔗 MRO (Method Resolution Order): {' -> '.join(mro_names)}")
        print(f"      📖 Help: \n        The order in which Python searches for methods. Shows inheritance hierarchy and method lookup path.\n")
    
    # Base classes
    if hasattr(obj_type, '__bases__'):
        base_names = [base.__name__ for base in obj_type.__bases__]
        print(f"    �️  __bases__: {base_names}")
        print(f"      📖 Help: \n        Direct parent classes this type inherits from. Shows immediate inheritance relationships.\n")
    
    # Size and memory
    try:
        size = sys.getsizeof(obj)
        print(f"    💾 Memory size: {size} bytes")
        print(f"      📖 Help: \n        Amount of memory this object occupies. Useful for understanding memory efficiency of different data types.\n")
    except:
        pass
    
    # Type attributes and methods count
    try:
        attrs = [attr for attr in dir(obj_type) if not attr.startswith('_')]
        methods = [attr for attr in attrs if callable(getattr(obj_type, attr, None))]
        print(f"    🔧 Public attributes: {len(attrs)}")
        print(f"    ⚙️  Public methods: {len(methods)}")
        print(f"      📖 Help: \n        Count of accessible attributes and methods. Shows the API surface of this data type.\n")
    except:
        pass
    
    # Special methods
    special_methods = [attr for attr in dir(obj) if attr.startswith('__') and attr.endswith('__') and callable(getattr(obj, attr, None))]
    if special_methods:
        print(f"    🎭 Special methods (__*__): {len(special_methods)} available")
        print(f"      📖 Help: \n        Dunder methods that implement Python's operator overloading and built-in behaviors.\n")
    
    print(f"\n    �🆔 the id({obj}) is {id(obj)}")
    print(f"      📖 Help: \n        Returns the unique identity of an object as an integer. This identity is guaranteed to be unique and constant for the object's lifetime, useful for checking if two variables reference the same object in memory.\n")
    
    print(f"    📝 the str({obj}) is {str(obj)}")
    print(f"      📖 Help: \n        Returns a string representation of the object intended for display to end users. This creates a readable, user-friendly string version of the object.\n")
    
    print(f"    💻 the repr({obj}) is {repr(obj)}")
    print(f"      📖 Help: \n        Returns the canonical string representation of the object, often more detailed than str(). This is meant for developers and should ideally be unambiguous - when possible, eval(repr(obj)) should recreate the object.\n")
    
    try:
        h = hash(obj)
        print(f"    🔒 the hash({obj}) is {h}")
        print(f"      📖 Help: \n        Returns an integer hash value for the object. Hash values are used in dictionaries and sets for fast lookups. Only immutable objects can be hashed.\n")
    except TypeError:
        print(f"    🚫 the hash({obj}) is Not hashable")
        print(f"      📖 Help: \n        This object cannot be hashed because it's mutable. Only immutable objects (like strings, numbers, tuples, frozensets) can be used as dictionary keys or set elements.\n")
    
    print(f"    ⚖️ the equality({obj} == {obj}) is {obj == obj}")
    
    # Identity vs equality
    print(f"    🆔 Identity check ({obj} is {obj}): {obj is obj}")
    print(f"      📖 Help: \n        Identity comparison checks if two references point to the same object in memory. More efficient than equality for singletons.\n")
    
    print(f"    🔍 the isinstance({obj}, {type(obj)}) is {isinstance(obj, type(obj))}")
    print(f"      📖 Help: \n        Checks if an object is an instance of a specific class or any of its subclasses. This is more flexible than checking exact type equality and is the preferred way to check object types in Python.\n")
    
    # Show some key attributes if they exist
    if hasattr(obj, '__dict__') and obj.__dict__:
        dict_items = list(obj.__dict__.items())[:3]  # Show first 3
        print(f"    📊 Instance __dict__: {len(obj.__dict__)} attributes")
        if dict_items:
            print(f"      📖 Sample: {dict_items}")
        print(f"      📖 Help: \n        Instance-specific attributes stored in this object's personal namespace.\n")

def demonstrate_int_operations(obj):
    """Demonstrates int-specific operations."""
    print(f"    ➕ {obj} + 8 = {obj + 8}")
    print(f"      📖 Help: \n        Addition operator adds two integers together. In education, this corresponds to combining student counts, adding points to scores, or calculating total attendance across classes.\n")
    print(f"    ✖️ {obj} * 2 = {obj * 2}")
    print(f"      📖 Help: \n        Multiplication operator multiplies two integers. Essential for scaling class sizes, calculating total points possible on assessments, or determining resource needs for multiple classes.\n")
    print(f"    ² {obj} ** 2 = {obj ** 2}")
    print(f"      📖 Help: \n        Exponentiation operator raises the number to a power. Squaring numbers is fundamental in geometry (area calculations), statistics (variance), and understanding exponential growth in populations or investments.\n")
    
    # Show int type documentation
    print(f"    📚 int.__doc__: {int.__doc__.split('.')[0] if int.__doc__ else 'No documentation'}.")
    print(f"      📖 Help: \n        Official Python documentation for the int type, explaining its purpose and behavior in the language.\n")

def demonstrate_float_operations(obj):
    """Demonstrates float-specific operations."""
    print(f"    ➕ {obj} + 1.86 = {obj + 1.86}")
    print(f"      📖 Help: \n        Addition with floating-point numbers. Essential for combining decimal values like test scores, calculating grade point averages, or adding fractional measurements in science experiments.\n")
    print(f"    ✖️ {obj} * 2 = {obj * 2}")
    print(f"      📖 Help: \n        Multiplication of floating-point numbers. Used for scaling percentages, calculating weighted grades, or determining proportional allocations of resources.\n")
    print(f"    ➗ {obj} / 2 = {obj / 2}")
    print(f"      📖 Help: \n        Division of floating-point numbers produces precise decimal results. Critical for calculating averages, percentages, rates of change, and statistical measures like mean and standard deviation.\n")

def demonstrate_complex_operations(obj):
    """Demonstrates complex-specific operations."""
    print(f"    ➕ {obj} + (1+2j) = {obj + (1 + 2j)}")
    print(f"      📖 Help: \n        Complex number addition adds real and imaginary parts separately. Foundational for advanced mathematics, electrical engineering (AC circuits), quantum physics, and signal processing analysis.\n")
    print(f"    ✖️ {obj} * (2+3j) = {obj * (2 + 3j)}")
    print(f"      📖 Help: \n        Complex multiplication follows (a+bi)(c+di) = (ac-bd) + (ad+bc)i. Essential for Fourier analysis, quantum mechanics calculations, and understanding wave phenomena in physics.\n")
    print(f"    ℝ {obj}.real = {obj.real}, ℑ {obj}.imag = {obj.imag}")
    print(f"      📖 Help: \n        Extracts real and imaginary components. Useful when you need to work with just one part of a complex result, such as separating magnitude and phase in signal analysis.\n")

def demonstrate_str_operations(obj):
    """Demonstrates string-specific operations."""
    print(f"    📏 len({obj}) = {len(obj)}")
    print(f"      📖 Help: \n        Returns the number of characters in the string. Essential for validating input lengths, counting words in essays, or ensuring responses meet minimum/maximum requirements.\n")
    print(f"    🔠 {obj}.upper() = {obj.upper()}")
    print(f"      📖 Help: \n        Converts text to uppercase. Useful for standardizing student names, creating headers, or normalizing text for case-insensitive comparisons in grading systems.\n")
    print(f"    ✂️ {obj}.split(', ') = {obj.split(', ')}")
    print(f"      📖 Help: \n        Splits strings into lists using delimiters. Perfect for parsing CSV data, separating student names, or breaking down complex responses into analyzable components.\n")
    
    # Show str type documentation
    print(f"    📚 str.__doc__: {str.__doc__.split('.')[0] if str.__doc__ else 'No documentation'}.")
    print(f"      📖 Help: \n        Official Python documentation for the str type, explaining how strings work as sequences of Unicode characters.\n")

def demonstrate_list_operations(obj):
    """Demonstrates list-specific operations."""
    # Create a copy to avoid modifying the original
    temp_list = obj.copy()
    temp_list.append(6)
    print(f"    ➕ {obj}.append(6) -> {temp_list}")
    print(f"      📖 Help: \n        Adds elements to lists dynamically. Perfect for building grade lists, collecting student responses over time, or accumulating data points in statistical analysis.\n")
    print(f"    🎯 {obj}[0] = {obj[0]}")
    print(f"      📖 Help: \n        Accesses elements by index (starting from 0). Fundamental for retrieving specific student records, accessing particular test scores, or working with ordered data collections.\n")
    print(f"    ✂️ {obj}[1:4] = {obj[1:4]}")
    print(f"      📖 Help: \n        Slicing extracts sublists. Essential for analyzing subsets of data, comparing performance ranges, or extracting specific time periods from longitudinal studies.\n")

def demonstrate_tuple_operations(obj):
    """Demonstrates tuple-specific operations."""
    print(f"    📏 len({obj}) = {len(obj)}")
    print(f"      📖 Help: \n        Returns the number of elements in the tuple. Useful for validating complete data sets, ensuring all required fields are present, or counting items in immutable collections.\n")
    print(f"    🎯 {obj}[2] = {obj[2]}")
    print(f"      📖 Help: \n        Accesses tuple elements by index. Perfect for retrieving specific components of structured data like coordinates, RGB color values, or fixed record fields.\n")
    print(f"    🔢 {obj}.count(3) = {obj.count(3)}")
    print(f"      📖 Help: \n        Counts occurrences of specific values. Essential for statistical analysis, identifying frequency distributions, or validating data integrity in immutable datasets.\n")

def demonstrate_range_operations(obj):
    """Demonstrates range-specific operations."""
    print(f"    📋 list({obj}) = {list(obj)}")
    print(f"      📖 Help: \n        Converts range to list to show all values. Ranges are memory-efficient for generating sequences like grade scales, time periods, or numbered assignments without storing all values.\n")
    print(f"    📊 list(range(0, 10, 2)) = {list(range(0, 10, 2))}")
    print(f"      📖 Help: \n        Creates arithmetic sequences with start, stop, and step. Perfect for generating even numbers, creating grading rubrics, or establishing regular intervals for data collection.\n")

def demonstrate_dict_operations(obj):
    """Demonstrates dict-specific operations."""
    print(f"    📝 list({obj}.keys()) = {list(obj.keys())}")
    print(f"      📖 Help: \n        Returns all dictionary keys (student names, IDs, etc.). Essential for iterating through records, generating reports, or accessing all entries in a gradebook.\n")
    print(f"    📊 list({obj}.values()) = {list(obj.values())}")
    print(f"      📖 Help: \n        Returns all dictionary values (grades, scores, etc.). Perfect for statistical analysis, calculating averages, or processing all data points without needing keys.\n")
    print(f"    🔍 {obj}.get('age', 'key not found') = {obj.get('age', 'key not found')}")
    print(f"      📖 Help: \n        Safely retrieves values with defaults. Prevents errors when accessing optional data fields, perfect for handling incomplete student records or missing assessment data.\n")
    # Don't modify the original dict
    temp_dict = obj.copy()
    temp_dict["new_key"] = "new_value"
    print(f"    ➕ {obj} with 'new_key' added = {temp_dict}")
    print(f"      📖 Help: \n        Adds new key-value pairs to dictionaries. Ideal for recording new student data, adding assessment results, or building comprehensive data records over time.\n")

def demonstrate_set_operations(obj):
    """Demonstrates set-specific operations."""
    # Create a copy to avoid modifying the original
    temp_set = obj.copy()
    temp_set.add(6)
    print(f"    ➕ {obj}.copy().add(6) = {temp_set}")
    print(f"      📖 Help: \n        Adds unique elements to sets. Perfect for tracking enrolled students, collecting unique responses, or maintaining lists where duplicates don't matter.\n")
    temp_set.remove(3) if 3 in temp_set else None
    print(f"    ➖ after remove(3) = {temp_set}")
    print(f"      📖 Help: \n        Removes specific elements from sets. Useful for updating enrollment lists, removing completed items, or managing dynamic collections of unique items.\n")
    set2 = {4, 5, 6, 7}
    print(f"    🔗 {obj} | {set2} = {temp_set | set2}")
    print(f"      📖 Help: \n        Union combines all unique elements. Essential for finding all students across multiple classes, combining survey responses, or merging different data sources.\n")
    print(f"    ⚡ {obj} & {set2} = {temp_set & set2}")
    print(f"      📖 Help: \n        Intersection finds common elements. Perfect for identifying students in multiple programs, finding overlapping skills, or analyzing shared characteristics.\n")

def demonstrate_frozenset_operations(obj):
    """Demonstrates frozenset-specific operations."""
    print(f"    🔗 {obj} | frozenset([4, 5]) = {obj | frozenset([4, 5])}")
    print(f"      📖 Help: \n        Performs union operation with immutable sets. Frozensets are perfect for core curriculum requirements, standardized test categories, or any fixed collection that serves as a reference.\n")

def demonstrate_bool_operations(obj):
    """Demonstrates bool-specific operations."""
    print(f"    🔗 {obj} and False = {obj and False}")
    print(f"      📖 Help: \n        Logical AND for combining conditions. Essential for eligibility checks (enrolled AND paid), validation rules (completed homework AND attended class), or complex decision trees.\n")
    print(f"    ➕ {obj} or False = {obj or False}")
    print(f"      📖 Help: \n        Logical OR for alternative conditions. Useful for flexible requirements (extra credit OR regular assignment), attendance policies, or grading alternatives.\n")
    print(f"    🔄 not {obj} = {not obj}")
    print(f"      📖 Help: \n        Logical NOT for inverting conditions. Perfect for checking absences (NOT present), failures (NOT passed), or creating inverse filters in data analysis.\n")

def demonstrate_bytes_operations(obj):
    """Demonstrates bytes-specific operations."""
    print(f"    🔓 {obj}.decode('utf-8') = {obj.decode('utf-8')}")
    print(f"      📖 Help: \n        Converts binary data to readable text. Essential for processing file uploads, network responses, or any encoded data in educational software and data exchange.\n")
    print(f"    📏 len({obj}) = {len(obj)}")
    print(f"      📖 Help: \n        Counts actual bytes in binary data. Important for file size validation, bandwidth calculations, or ensuring data integrity when bytes ≠ characters in encoding.\n")

def demonstrate_bytearray_operations(obj):
    """Demonstrates bytearray-specific operations."""
    # Create a copy to avoid modifying the original
    temp_array = bytearray(obj)
    temp_array[0] = 72
    print(f"    ✏️ {obj} with [0] = 72 = {temp_array}")
    print(f"      📖 Help: \n        Modifies binary data in-place. Perfect for editing image files, processing audio data, or updating binary records without creating new objects.\n")
def demonstrate_memoryview_operations(obj):
    """Demonstrates memoryview-specific operations."""
    print(f"    📋 list({obj}) = {list(obj)}")
    print(f"      📖 Help: \n        Provides zero-copy access to binary data. Memory-efficient for large datasets, perfect for analyzing big educational data files without duplicating memory.\n")
    print(f"      📖 Help: \n        Enables efficient data sharing across functions. Ideal for passing large binary datasets to analysis functions without the memory overhead of copying.\n")

def demonstrate_none_operations(obj):
    """Demonstrates None-specific operations."""
    print(f"    ❓ {obj} is None = {obj is None}")
    print(f"      📖 Help: \n        Identity check for missing data. Preferred method for detecting ungraded assignments, absent students, or incomplete data records in educational databases.\n")
    print(f"    ❓ {obj} == None = {obj == None}")
    print(f"      📖 Help: \n        Equality check with None. While functional, 'is None' is more efficient and Pythonic for checking missing values in student records or assessment data.\n")

# Type-specific operation dispatch
type_operations = {
    int: demonstrate_int_operations,
    float: demonstrate_float_operations,
    complex: demonstrate_complex_operations,
    str: demonstrate_str_operations,
    list: demonstrate_list_operations,
    tuple: demonstrate_tuple_operations,
    range: demonstrate_range_operations,
    dict: demonstrate_dict_operations,
    set: demonstrate_set_operations,
    frozenset: demonstrate_frozenset_operations,
    bool: demonstrate_bool_operations,
    bytes: demonstrate_bytes_operations,
    bytearray: demonstrate_bytearray_operations,
    memoryview: demonstrate_memoryview_operations,
    type(None): demonstrate_none_operations,
}

# 1. Numeric Types - Educational Examples
# Integers are perfect for counting discrete items like student counts, test questions, or attendance numbers
student_count = 42                    # int - number of students in a class
# Floats handle measurements and calculations with decimals, essential for grades, percentages, and statistical analysis
average_score = 85.7                  # float - average test score percentage
# Complex numbers appear in advanced mathematics and physics, useful for electrical engineering and signal processing concepts
complex_coefficient = 3 + 4j          # complex - complex numbers in advanced mathematics

def interactive_menu():
    print("\n🎓 INTERACTIVE LEARNING ENVIRONMENT")
    print("This menu uses a layered approach: Surface → Intermediate → Deep → Core")
    print("Each exploration combines explanations with live demonstrations.")
    press_enter_to_continue("Ready to start interactive learning?")

    while True:
        print("\n" + "=" * 60)
        print("🎮 INTERACTIVE EXPERIMENTATION MENU")
        print("=" * 60)
        print("Choose a data type to explore through four learning levels:")
        print("1. 📊 Numbers (integers and floats)")
        print("2. 📝 Text (strings)")
        print("3. 📋 Lists (collections)")
        print("4. 🗺️ Dictionaries (key-value mappings)")
        print("5. 🔄 Sets (unique collections)")
        print("6. ✅ Booleans (true/false)")
        print("7. 🚪 Exit interactive mode")
        print("=" * 60)

        try:
            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == '1':
                # Ask user what type of numbers to explore
                print("\n📊 NUMBERS - Choose your number type!")
                print("1. Integers (whole numbers like 42, -7, 1000)")
                print("2. Floats (decimal numbers like 3.14, -2.5, 85.7)")

                num_choice = input("Enter 1 for integers or 2 for floats: ").strip()

                if num_choice == '1':
                    # Integer exploration
                    print("\n� INTEGERS - Let's create some whole numbers to explore!")
                    num1 = int(input("Enter first integer (e.g., 42 for a count): "))
                    num2 = int(input("Enter second integer (e.g., 85 for a score): "))
                    interactive_integers_layered(num1, num2)
                elif num_choice == '2':
                    # Float exploration
                    print("\n📊 FLOATS - Let's create some decimal numbers to explore!")
                    num1 = float(input("Enter first decimal (e.g., 85.5 for a grade): "))
                    num2 = float(input("Enter second decimal (e.g., 92.3 for another grade): "))
                    interactive_floats_layered(num1, num2)
                else:
                    print("❌ Please enter 1 or 2.")
                    continue
            elif choice == '2':
                # Get user input first, then explore
                print("\n📝 TEXT - Let's create some text to explore!")
                text = input("Enter some text (e.g., student names or feedback): ")
                interactive_strings_layered(text)
            elif choice == '3':
                # Get user input first, then explore
                print("\n📋 LISTS - Let's create a list to explore!")
                scores_input = input("Enter test scores separated by commas (e.g., 85,92,78,96): ")
                scores = [float(score.strip()) for score in scores_input.split(',')]
                interactive_lists_layered(scores)
            elif choice == '4':
                # Get user input first, then explore
                print("\n🗺️ DICTIONARIES - Let's create a grade book to explore!")
                students = {}
                while True:
                    name = input("Enter student name (or 'done' to finish): ").strip()
                    if name.lower() == 'done':
                        break
                    grade = float(input(f"Enter grade for {name}: "))
                    students[name] = grade
                interactive_dicts_layered(students)
            elif choice == '5':
                # Get user input first, then explore
                print("\n🔄 SETS - Let's create subject sets to explore!")
                subjects1_input = input("Enter subjects for class A (comma-separated): ")
                subjects2_input = input("Enter subjects for class B (comma-separated): ")
                class_a = set(subject.strip() for subject in subjects1_input.split(','))
                class_b = set(subject.strip() for subject in subjects2_input.split(','))
                interactive_sets_layered(class_a, class_b)
            elif choice == '6':
                # Get user input first, then explore
                print("\n✅ BOOLEANS - Let's create conditions to explore!")
                attendance = input("Did the student attend class? (yes/no): ").strip().lower() == 'yes'
                homework = input("Did the student complete homework? (yes/no): ").strip().lower() == 'yes'
                exam = input("Did the student pass the exam? (yes/no): ").strip().lower() == 'yes'
                interactive_booleans_layered(attendance, homework, exam)
            elif choice == '7':
                print("\n👋 Thanks for exploring Python data types!")
                print("🎓 Remember: Every data type has surface behavior and deep internal mechanics!")
                break
            else:
                print("❌ Please enter a number between 1 and 7.")

        except KeyboardInterrupt:
            print("\n👋 Interactive session ended.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def interactive_integers_layered(num1, num2):
    """Interactive deep introspection of integer values using layered learning approach."""
    print("\n🔢 INTERACTIVE INTEGERS - FROM SURFACE TO CORE")
    print("We'll explore whole numbers through four learning levels with live demonstrations.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("🔢 INTEGER TYPES INTERACTIONS")
    print("=" * 60)

    # Use the provided integers for demonstrations
    student_count = num1 if isinstance(num1, int) else int(num1)
    class_size = num2 if isinstance(num2, int) else int(num2)

    print(f"Student Count ({student_count}):")
    print(f"  + 5 = {student_count + 5}")
    print(f"  * 3 = {student_count * 3}")
    print(f"  ** 2 = {student_count ** 2}")
    print(f"  // 2 = {student_count // 2} (integer division)")

    print(f"\nClass Size ({class_size}):")
    print(f"  - 2 = {class_size - 2}")
    print(f"  % 10 = {class_size % 10} (remainder when divided by 10)")
    print(f"  Is even: {class_size % 2 == 0}")

    press_enter_to_continue("Ready to explore these integers through layered learning?")

    try:
        # Level 1: Surface - Basic input and type identification
        show_learning_level(1, "Surface Level", "Understanding what integers look like and their basic properties")
        press_enter_to_continue("Ready to analyze these integers?")

        print(f"\n🔍 LEVEL 1 ANALYSIS: {num1} and {num2}")
        print(f"    📊 Type: {type(num1).__name__} and {type(num2).__name__}")
        print(f"        → What kind of data this is (int, float, str, etc.)")
        print(f"        → Use type() function to check: type({num1}) → {type(num1)}")
        print(f"    📝 String representation: '{num1}' and '{num2}'")
        print(f"        → How Python displays this for humans (using str() function)")
        print(f"        → str({num1}) → '{str(num1)}', str({num2}) → '{str(num2)}'")
        print(f"    💻 Repr representation: {repr(num1)} and {repr(num2)}")
        print(f"        → Exact representation for developers/debugging (using repr() function)")
        print(f"        → repr({num1}) → {repr(num1)}, repr({num2}) → {repr(num2)}")
        print(f"        → Shows quotes for strings, exact decimal for floats")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Practical operations and educational context
        show_learning_level(2, "Intermediate Level", "How integers behave in real educational calculations")
        press_enter_to_continue("See how these integers work in practice?")

        operations = [
            ("Addition", num1 + num2, "Combining student counts"),
            ("Subtraction", num1 - num2, "Finding differences"),
            ("Multiplication", num1 * num2, "Calculating totals"),
            ("Integer Division", num1 // num2 if num2 != 0 else "Undefined", "Dividing into groups"),
            ("Modulo", num1 % num2 if num2 != 0 else "Undefined", "Finding remainders"),
        ]

        print(f"    🧮 PRACTICAL OPERATIONS:")
        for op_name, result, context in operations:
            print(f"      {op_name}: {num1} {op_name[0].lower() if op_name != 'Integer Division' and op_name != 'Modulo' else '//' if op_name == 'Integer Division' else '%'} {num2} = {result}")
            print(f"        📖 Educational use: {context}")

        # Educational context
        total = num1 + num2
        if total > 0:
            print(f"    🎓 Total students: {total}")
            print(f"    📊 Average per class: {total // 2}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - Internal representations and memory
        show_learning_level(3, "Deep Level", "How Python stores and processes integers internally")
        press_enter_to_continue("Dive into Python's internal integer handling?")

        for i, num in enumerate([num1, num2], 1):
            print(f"    🔬 INTEGER {i} INTERNAL ANALYSIS:")
            print(f"      🆔 Memory address: {hex(id(num))} (where this integer lives in RAM)")
            print(f"      💾 Memory size: {sys.getsizeof(num)} bytes (space it takes up)")
            print(f"      🔢 Binary: {bin(num)} (number in base-2, just 0s and 1s)")
            print(f"      🔢 Hexadecimal: {hex(num)} (number in base-16, compact format)")
            print(f"      📊 Bit length: {num.bit_length()} bits (how many binary digits needed)")
            print(f"      🔒 Hash value: {hash(num)} (unique fingerprint for this integer)")
            print(f"      📊 Reference count: {sys.getrefcount(num)} (how many variables point to it)")

        # Level 4: Core - System integration and bytecode
        show_learning_level(4, "Core Level", "How integers integrate with Python's C runtime and execution model")
        press_enter_to_continue("Explore the core system level?")

        print(f"    🧬 PYTHON'S INTEGER SYSTEM:")
        print(f"      Let's understand how Python handles whole numbers...")

        print(f"      • int objects: PyLongObject (arbitrary precision C integers)")
        print(f"        → Python can handle HUGE integers limited only by available memory")
        print(f"      • No overflow: Unlike C/Java, Python integers grow as needed")
        print(f"      • Operations: Compiled to optimized C function calls")
        print(f"        → Your + and * become super-fast machine code")
        print(f"      • Memory: Managed by Python's garbage collector")

        press_enter_to_continue("See how Python code becomes machine instructions?")

        # Show bytecode of a simple calculation
        def demo_calculation(a, b):
            return a + b * 2

        print(f"    📋 HOW PYTHON RUNS YOUR CODE:")
        print(f"      When you write: return a + b * 2")
        print(f"      Python creates: bytecode (intermediate instructions)")
        print(f"      Then executes: optimized machine code")
        print(f"      ")
        print(f"      📋 BYTECODE EXAMPLE (what Python actually runs):")
        dis.dis(demo_calculation)
        print(f"      ")
        print(f"      🔍 BYTECODE INSTRUCTIONS EXPLAINED:")
        print(f"        RESUME: Prepare to run this function")
        print(f"        LOAD_FAST: Get variable from function's local storage")
        print(f"          → LOAD_FAST(0): Get parameter 'a' from position 0")
        print(f"          → LOAD_FAST(1): Get parameter 'b' from position 1")
        print(f"        LOAD_CONST: Get a constant value (like the number 2)")
        print(f"          → LOAD_CONST(1): Get the constant 2")
        print(f"        BINARY_OP: Perform a math operation")
        print(f"          → BINARY_OP(5): Multiply (*) the top two values")
        print(f"          → BINARY_OP(0): Add (+) the top two values")
        print(f"        RETURN_VALUE: Send result back to caller")
        print(f"      ")
        print(f"      💡 Why bytecode? It's platform-independent and gets optimized!")

        press_enter_to_continue("See the complete journey?")

        print(f"    🎯 KEY INSIGHT: Integers are C structures with Python interfaces!")
        print(f"      Your math becomes: Source Code → AST → Bytecode → C Functions → Results")
        print(f"      → AST: Abstract Syntax Tree (code structure)")
        print(f"      → Bytecode: Python's intermediate language")
        print(f"      → C Functions: Fast compiled machine code")

    except ValueError:
        print("❌ Please enter valid integers!")
    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_floats_layered(num1, num2):
    """Interactive deep introspection of float values using layered learning approach."""
    print("\n📊 INTERACTIVE FLOATS - FROM SURFACE TO CORE")
    print("We'll explore decimal numbers through four learning levels with live demonstrations.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("📊 FLOAT TYPES INTERACTIONS")
    print("=" * 60)

    # Use the provided floats for demonstrations
    grade1 = float(num1)
    grade2 = float(num2)

    print(f"Grade 1 ({grade1}):")
    print(f"  + 1.5 = {grade1 + 1.5}")
    print(f"  * 1.1 = {grade1 * 1.1}")
    print(f"  Rounded to 1 decimal: {round(grade1, 1)}")

    print(f"\nGrade 2 ({grade2}):")
    print(f"  - 0.5 = {grade2 - 0.5}")
    print(f"  / 2 = {grade2 / 2}")
    print(f"  Is whole number: {grade2.is_integer()}")

    press_enter_to_continue("Ready to explore these floats through layered learning?")

    try:
        # Level 1: Surface - Basic input and type identification
        show_learning_level(1, "Surface Level", "Understanding what floats look like and their basic properties")
        press_enter_to_continue("Ready to analyze these floats?")

        print(f"\n🔍 LEVEL 1 ANALYSIS: {num1} and {num2}")
        print(f"    📊 Type: {type(num1).__name__} and {type(num2).__name__}")
        print(f"        → What kind of data this is (int, float, str, etc.)")
        print(f"        → Use type() function to check: type({num1}) → {type(num1)}")
        print(f"    📝 String representation: '{num1}' and '{num2}'")
        print(f"        → How Python displays this for humans (using str() function)")
        print(f"        → str({num1}) → '{str(num1)}', str({num2}) → '{str(num2)}'")
        print(f"    💻 Repr representation: {repr(num1)} and {repr(num2)}")
        print(f"        → Exact representation for developers/debugging (using repr() function)")
        print(f"        → repr({num1}) → {repr(num1)}, repr({num2}) → {repr(num2)}")
        print(f"        → Shows quotes for strings, exact decimal for floats")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Practical operations and educational context
        show_learning_level(2, "Intermediate Level", "How floats behave in real educational calculations")
        press_enter_to_continue("See how these floats work in practice?")

        operations = [
            ("Addition", num1 + num2, "Combining grade points"),
            ("Subtraction", num1 - num2, "Finding grade differences"),
            ("Multiplication", num1 * num2, "Calculating weighted scores"),
            ("Division", num1 / num2 if num2 != 0 else "Undefined", "Finding averages"),
        ]

        print(f"    🧮 PRACTICAL OPERATIONS:")
        for op_name, result, context in operations:
            print(f"      {op_name}: {num1} {op_name[0].lower() if op_name != 'Division' else '/'} {num2} = {result}")
            print(f"        📖 Educational use: {context}")

        # Educational context
        avg = (num1 + num2) / 2
        if 0 <= avg <= 100:
            grade = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"
            print(f"    🎓 Class average: {avg:.2f} → Grade: {grade}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - Internal representations and memory
        show_learning_level(3, "Deep Level", "How Python stores and processes floats internally")
        press_enter_to_continue("Dive into Python's internal float handling?")

        for i, num in enumerate([num1, num2], 1):
            print(f"    🔬 FLOAT {i} INTERNAL ANALYSIS:")
            print(f"      🆔 Memory address: {hex(id(num))} (where this float lives in RAM)")
            print(f"      💾 Memory size: {sys.getsizeof(num)} bytes (space it takes up)")
            print(f"      🔢 IEEE 754 hex: {num.hex()} (standard way computers store decimals)")
            print(f"      🔢 Mantissa/Exponent: {num.as_integer_ratio()} (fraction as whole numbers)")
            print(f"        → Mantissa: the numerator, Exponent: power of 2 to multiply by")
            print(f"      ✅ Is finite: {num.is_integer()} (can it be written without decimal part?)")
            print(f"      🔒 Hash value: {hash(num)} (unique fingerprint for this float)")
            print(f"      📊 Reference count: {sys.getrefcount(num)} (how many variables point to it)")

        # Level 4: Core - System integration and bytecode
        show_learning_level(4, "Core Level", "How floats integrate with Python's C runtime and execution model")
        press_enter_to_continue("Explore the core system level?")

        print(f"    🧬 PYTHON'S FLOAT SYSTEM:")
        print(f"      Let's understand how Python handles decimal numbers...")

        print(f"      • float objects: PyFloatObject (IEEE 754 double precision)")
        print(f"        → Uses the same decimal standard as calculators and computers worldwide")
        print(f"      • Precision limits: About 15 decimal digits of precision")
        print(f"      • Operations: Compiled to optimized C function calls")
        print(f"        → Your + and * become super-fast machine code")
        print(f"      • Memory: Managed by Python's garbage collector")

        press_enter_to_continue("See how Python code becomes machine instructions?")

        # Show bytecode of a simple calculation
        def demo_calculation(a, b):
            return a + b * 2.0

        print(f"    📋 HOW PYTHON RUNS YOUR CODE:")
        print(f"      When you write: return a + b * 2.0")
        print(f"      Python creates: bytecode (intermediate instructions)")
        print(f"      Then executes: optimized machine code")
        print(f"      ")
        print(f"      📋 BYTECODE EXAMPLE (what Python actually runs):")
        dis.dis(demo_calculation)
        print(f"      ")
        print(f"      🔍 BYTECODE INSTRUCTIONS EXPLAINED:")
        print(f"        RESUME: Prepare to run this function")
        print(f"        LOAD_FAST: Get variable from function's local storage")
        print(f"          → LOAD_FAST(0): Get parameter 'a' from position 0")
        print(f"          → LOAD_FAST(1): Get parameter 'b' from position 1")
        print(f"        LOAD_CONST: Get a constant value (like the number 2.0)")
        print(f"          → LOAD_CONST(1): Get the constant 2.0")
        print(f"        BINARY_OP: Perform a math operation")
        print(f"          → BINARY_OP(5): Multiply (*) the top two values")
        print(f"          → BINARY_OP(0): Add (+) the top two values")
        print(f"        RETURN_VALUE: Send result back to caller")
        print(f"      ")
        print(f"      💡 Why bytecode? It's platform-independent and gets optimized!")

        press_enter_to_continue("See the complete journey?")

        print(f"    🎯 KEY INSIGHT: Floats are C structures with Python interfaces!")
        print(f"      Your math becomes: Source Code → AST → Bytecode → C Functions → Results")
        print(f"      → AST: Abstract Syntax Tree (code structure)")
        print(f"      → Bytecode: Python's intermediate language")
        print(f"      → C Functions: Fast compiled machine code")

    except ValueError:
        print("❌ Please enter valid floats!")
    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_numbers_layered(num1, num2):
    """Interactive deep introspection of numeric values using layered learning approach."""
    print("\n🧬 INTERACTIVE NUMBERS - FROM SURFACE TO CORE")
    print("We'll explore numbers through four learning levels with live demonstrations.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("1. 📊 NUMERIC TYPES INTERACTIONS")
    print("=" * 60)

    # Use the provided numbers for demonstrations
    student_count = int(num1) if num1 >= 0 else 42
    average_score = float(num2) if num2 > 0 else 85.7
    complex_coefficient = 3 + 4j

    print(f"Student Count ({student_count}):")
    print(f"  + 8 = {student_count + 8}")
    print(f"  * 2 = {student_count * 2}")
    print(f"  ** 2 = {student_count ** 2}")

    print(f"\nAverage Score ({average_score}):")
    print(f"  + 1.86 = {average_score + 1.86}")
    print(f"  * 2 = {average_score * 2}")
    print(f"  / 2 = {average_score / 2}")

    print(f"\nComplex Coefficient ({complex_coefficient}):")
    print(f"  + (1+2j) = {complex_coefficient + (1 + 2j)}")
    print(f"  * (2+3j) = {complex_coefficient * (2 + 3j)}")
    print(f"  Real part: {complex_coefficient.real}, Imaginary part: {complex_coefficient.imag}")

    press_enter_to_continue("Ready to explore these numbers through layered learning?")

    try:
        # Level 1: Surface - Basic input and type identification
        show_learning_level(1, "Surface Level", "Understanding what numbers look like and their basic properties")
        press_enter_to_continue("Ready to analyze these numbers?")

        print(f"\n🔍 LEVEL 1 ANALYSIS: {num1} and {num2}")
        print(f"    📊 Type: {type(num1).__name__} and {type(num2).__name__}")
        print(f"        → What kind of data this is (int, float, str, etc.)")
        print(f"        → Use type() function to check: type({num1}) → {type(num1)}")
        print(f"    📝 String representation: '{num1}' and '{num2}'")
        print(f"        → How Python displays this for humans (using str() function)")
        print(f"        → str({num1}) → '{str(num1)}', str({num2}) → '{str(num2)}'")
        print(f"    💻 Repr representation: {repr(num1)} and {repr(num2)}")
        print(f"        → Exact representation for developers/debugging (using repr() function)")
        print(f"        → repr({num1}) → {repr(num1)}, repr({num2}) → {repr(num2)}")
        print(f"        → Shows quotes for strings, exact decimal for floats")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Practical operations and educational context
        show_learning_level(2, "Intermediate Level", "How numbers behave in real educational calculations")
        press_enter_to_continue("See how these numbers work in practice?")

        operations = [
            ("Addition", num1 + num2, "Combining student scores"),
            ("Subtraction", num1 - num2, "Finding score differences"),
            ("Multiplication", num1 * num2, "Scaling grades or calculating totals"),
            ("Division", num1 / num2 if num2 != 0 else "Undefined", "Finding averages or percentages"),
        ]

        print(f"    🧮 PRACTICAL OPERATIONS:")
        for op_name, result, context in operations:
            print(f"      {op_name}: {num1} {op_name[0].lower() if op_name != 'Division' else '/'} {num2} = {result}")
            print(f"        📖 Educational use: {context}")

        # Educational context
        avg = (num1 + num2) / 2
        if 0 <= avg <= 100:
            grade = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"
            print(f"    🎓 Class average: {avg:.2f} → Grade: {grade}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - Internal representations and memory
        show_learning_level(3, "Deep Level", "How Python stores and processes numbers internally")
        press_enter_to_continue("Dive into Python's internal number handling?")

        for i, num in enumerate([num1, num2], 1):
            print(f"    🔬 NUMBER {i} INTERNAL ANALYSIS:")
            print(f"      🆔 Memory address: {hex(id(num))} (where this number lives in RAM)")
            print(f"      💾 Memory size: {sys.getsizeof(num)} bytes (space it takes up)")

            if isinstance(num, int):
                print(f"      🔢 Binary: {bin(num)} (number in base-2, just 0s and 1s)")
                print(f"      🔢 Hexadecimal: {hex(num)} (number in base-16, compact format)")
                print(f"      📊 Bit length: {num.bit_length()} bits (how many binary digits needed)")
            elif isinstance(num, float):
                print(f"      🔢 IEEE 754 hex: {num.hex()} (standard way computers store decimals)")
                print(f"      🔢 Mantissa/Exponent: {num.as_integer_ratio()} (fraction as whole numbers)")
                print(f"        → Mantissa: the numerator, Exponent: power of 2 to multiply by")
                print(f"      ✅ Is finite: {num.is_integer()} (can it be written without decimal part?)")

            print(f"      🔒 Hash value: {hash(num)} (unique fingerprint for this number)")
            print(f"      📊 Reference count: {sys.getrefcount(num)} (how many variables point to it)")

        # Level 4: Core - System integration and bytecode
        show_learning_level(4, "Core Level", "How numbers integrate with Python's C runtime and execution model")
        press_enter_to_continue("Explore the core system level?")

        # Level 4: Core - System integration and bytecode
        show_learning_level(4, "Core Level", "How numbers integrate with Python's C runtime and execution model")
        press_enter_to_continue("Explore the core system level?")

        print(f"    🧬 PYTHON'S NUMBER SYSTEM:")
        print(f"      Let's understand how Python numbers work under the hood...")

        print(f"      • int objects: PyLongObject (arbitrary precision C integers)")
        print(f"        → Python can handle HUGE numbers limited only by available memory")
        print(f"      • float objects: PyFloatObject (IEEE 754 double precision)")
        print(f"        → Uses the same decimal standard as calculators and computers worldwide")
        print(f"      • Operations: Compiled to optimized C function calls")
        print(f"        → Your + and * become super-fast machine code")
        print(f"      • Memory: Managed by Python's garbage collector")
        print(f"        → Python automatically cleans up unused numbers")

        press_enter_to_continue("See how Python code becomes machine instructions?")

        # Show bytecode of a simple calculation
        def demo_calculation(a, b):
            return a + b * 2

        print(f"    📋 HOW PYTHON RUNS YOUR CODE:")
        print(f"      When you write: return a + b * 2")
        print(f"      Python creates: bytecode (intermediate instructions)")
        print(f"      Then executes: optimized machine code")
        print(f"      ")
        print(f"      📋 BYTECODE EXAMPLE (what Python actually runs):")
        dis.dis(demo_calculation)
        print(f"      ")
        print(f"      🔍 BYTECODE INSTRUCTIONS EXPLAINED:")
        print(f"        RESUME: Prepare to run this function")
        print(f"        LOAD_FAST: Get variable from function's local storage")
        print(f"          → LOAD_FAST(0): Get parameter 'a' from position 0")
        print(f"          → LOAD_FAST(1): Get parameter 'b' from position 1")
        print(f"        LOAD_CONST: Get a constant value (like the number 2)")
        print(f"          → LOAD_CONST(1): Get the constant 2")
        print(f"        BINARY_OP: Perform a math operation")
        print(f"          → BINARY_OP(5): Multiply (*) the top two values")
        print(f"          → BINARY_OP(0): Add (+) the top two values")
        print(f"        RETURN_VALUE: Send result back to caller")
        print(f"      ")
        print(f"      💡 Why bytecode? It's platform-independent and gets optimized!")

        press_enter_to_continue("See the complete journey?")

        print(f"    🎯 KEY INSIGHT: Numbers are C structures with Python interfaces!")
        print(f"      Your math becomes: Source Code → AST → Bytecode → C Functions → Results")
        print(f"      → AST: Abstract Syntax Tree (code structure)")
        print(f"      → Bytecode: Python's intermediate language")
        print(f"      → C Functions: Fast compiled machine code")

    except ValueError:
        print("❌ Please enter valid numbers!")
    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_strings_layered(text):
    """Interactive string exploration using layered learning approach."""
    print("\n📝 INTERACTIVE STRINGS - FROM SURFACE TO CORE")
    print("We'll explore text through four learning levels with live demonstrations.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("2. 📝 SEQUENCE TYPES INTERACTIONS (STRINGS)")
    print("=" * 60)

    # Use the provided text for demonstrations
    student_names = text if text else "Alice, Bob, Charlie, Diana"

    print(f"Student Names ('{student_names}'):")
    print(f"  Length: {len(student_names)}")
    print(f"  Uppercase: {student_names.upper()}")
    print(f"  Split by ', ': {student_names.split(', ')}")

    press_enter_to_continue("Ready to explore this text through layered learning?")

    try:
        # Level 1: Surface - Basic input and properties
        show_learning_level(1, "Surface Level", "Understanding what strings look like and their basic properties")
        press_enter_to_continue("Ready to analyze this text?")

        print(f"\n🔍 LEVEL 1 ANALYSIS: '{text}'")
        print(f"    📊 Type: {type(text).__name__}")
        print(f"    📏 Length: {len(text)} characters")
        print(f"    📝 String representation: '{str(text)}'")
        print(f"    💻 Repr representation: {repr(text)}")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Practical text operations
        show_learning_level(2, "Intermediate Level", "How strings behave in real educational scenarios")
        press_enter_to_continue("See how this text can be used in education?")

        print(f"    🔄 TEXT TRANSFORMATIONS:")
        print(f"      🔠 Uppercase: '{text.upper()}'")
        print(f"      🔡 Lowercase: '{text.lower()}'")
        print(f"      ✏️ Title case: '{text.title()}'")

        if ',' in text:
            names = [name.strip() for name in text.split(',')]
            print(f"      👥 Split by comma: {names}")
            print(f"      👨‍👩‍👧‍👦 Student count: {len(names)}")
        elif ' ' in text:
            words = text.split()
            print(f"      📝 Split by space: {words}")
            print(f"      📊 Word count: {len(words)}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - String internals and encoding
        show_learning_level(3, "Deep Level", "How Python stores and processes text internally")
        press_enter_to_continue("Dive into how Python handles text internally?")

        print(f"    🔬 STRING INTERNAL ANALYSIS:")
        print(f"      🆔 Memory address: {hex(id(text))} (where this text lives in RAM)")
        print(f"      💾 Memory size: {sys.getsizeof(text)} bytes (space it takes up)")
        print(f"      🔒 Hash value: {hash(text)} (unique fingerprint for this text)")
        print(f"      📊 Reference count: {sys.getrefcount(text)} (how many variables point to it)")

        # Character analysis
        chars = list(text)
        unique_chars = set(chars)
        print(f"      🔤 Characters: {chars}")
        print(f"      🎯 Unique characters: {len(unique_chars)}")
        print(f"      🔢 Character codes: {[ord(c) for c in chars[:5]]}... (Unicode numbers for each character)")

        # Level 4: Core - Unicode and system integration
        show_learning_level(4, "Core Level", "How strings integrate with Unicode and Python's text processing")
        press_enter_to_continue("Explore Unicode and text encoding?")

        print(f"    🧬 PYTHON'S TEXT SYSTEM:")
        print(f"      Let's understand how Python handles all the world's writing systems...")

        print(f"      • String objects: PyUnicodeObject (Unicode text)")
        print(f"        → Supports every language: English, Chinese, Arabic, emojis, etc.")
        print(f"      • Encoding: UTF-8 by default, supports all Unicode characters")
        print(f"        → UTF-8: Universal standard for storing text as bytes")
        print(f"      • Immutability: Strings cannot be modified in-place")
        print(f"        → Every change creates a new string (that's why text is 'safe')")

        press_enter_to_continue("See how text becomes computer bytes?")

        # Show encoding details
        encoded = text.encode('utf-8')
        print(f"      🔄 UTF-8 encoded: {encoded}")
        print(f"        → Your text as numbers that computers understand")
        print(f"      📏 Encoded size: {len(encoded)} bytes")
        print(f"        → How many bytes needed to store this text")
        print(f"      🔓 Decoded back: {encoded.decode('utf-8')}")
        print(f"        → Converting bytes back to readable text")

        print(f"    🎯 KEY INSIGHT: Text is Unicode with Python interfaces!")
        print(f"      Your strings become: Characters → Unicode → UTF-8 → Display")

    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_lists_layered(scores):
    """Interactive list exploration using layered learning approach."""
    print("\n📋 INTERACTIVE LISTS - FROM SURFACE TO CORE")
    print("We'll explore collections through four learning levels with live demonstrations.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("2. 📝 SEQUENCE TYPES INTERACTIONS (LISTS)")
    print("=" * 60)

    # Use the provided scores for demonstrations
    test_scores = scores.copy() if scores else [85, 92, 78, 96, 88]

    print(f"Test Scores ({test_scores}):")
    test_scores.append(91)
    print(f"  After append(91): {test_scores}")
    print(f"  Index [0]: {test_scores[0]}")
    print(f"  Slice [1:4]: {test_scores[1:4]}")

    press_enter_to_continue("Ready to explore this list through layered learning?")

    try:
        # Level 1: Surface - Basic input and properties
        show_learning_level(1, "Surface Level", "Understanding what lists look like and their basic properties")
        press_enter_to_continue("Ready to analyze this list of scores?")

        print(f"\n🔍 LEVEL 1 ANALYSIS: {scores}")
        print(f"    📊 Type: {type(scores).__name__}")
        print(f"    📏 Length: {len(scores)} items")
        print(f"    📝 String representation: {str(scores)}")
        print(f"    💻 Repr representation: {repr(scores)}")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Practical list operations
        show_learning_level(2, "Intermediate Level", "How lists behave in real educational data processing")
        press_enter_to_continue("See how this list can be used for grade analysis?")

        print(f"    📊 STATISTICAL ANALYSIS:")
        print(f"      📈 Highest score: {max(scores)}")
        print(f"      📉 Lowest score: {min(scores)}")
        print(f"      📊 Average: {sum(scores) / len(scores):.2f}")
        print(f"      📋 Sorted: {sorted(scores)}")

        # Add a new score
        new_score = float(input("Enter a new score to add: "))
        scores.append(new_score)
        print(f"      ➕ After adding {new_score}: {scores}")
        print(f"      📊 New average: {sum(scores) / len(scores):.2f}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - List internals and mutability
        show_learning_level(3, "Deep Level", "How Python stores and manages mutable collections")
        press_enter_to_continue("Explore how lists work internally?")

        print(f"    🔬 LIST INTERNAL ANALYSIS:")
        print(f"      🆔 Memory address: {hex(id(scores))} (where this list lives in RAM)")
        print(f"      💾 Memory size: {sys.getsizeof(scores)} bytes (space it takes up)")
        print(f"      🚫 Not hashable (mutable type)")
        print(f"        → Lists can change, so they can't be used as dictionary keys")

        # Show element addresses
        print(f"      📍 Element addresses:")
        for i, score in enumerate(scores[:3]):  # Show first 3
            print(f"        [{i}]: {hex(id(score))} → {score}")
        print(f"        → Each item in the list has its own memory location")

        # Level 4: Core - Dynamic arrays and memory management
        show_learning_level(4, "Core Level", "How lists integrate with Python's dynamic memory system")
        press_enter_to_continue("Explore list memory management?")

        print(f"    🧬 PYTHON'S LIST SYSTEM:")
        print(f"      Let's understand how Python makes lists flexible and efficient...")

        print(f"      • List objects: PyListObject (dynamic arrays)")
        print(f"        → Like a resizable container that grows as you add items")
        print(f"      • Growth: Lists over-allocate space for efficiency")
        print(f"        → Reserves extra space so adding items is fast")
        print(f"      • References: Store references to objects, not copies")
        print(f"        → Points to your data instead of duplicating it")

        # Show capacity concept
        print(f"      📊 Current size: {len(scores)} items")
        print(f"      💾 Allocated space: ~{sys.getsizeof(scores)} bytes")
        print(f"      🔄 Mutable: Can add/remove/modify elements")
        print(f"        → Unlike strings, lists can change after creation")

        print(f"    🎯 KEY INSIGHT: Lists are dynamic arrays with Python interfaces!")
        print(f"      Your collections become: Objects → References → Dynamic Array → Access")

    except ValueError:
        print("❌ Please enter valid numbers separated by commas!")
    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_dicts_layered(students):
    """Interactive dictionary exploration using layered learning approach."""
    print("\n🗺️ INTERACTIVE DICTIONARIES - FROM SURFACE TO CORE")
    print("We'll explore mappings through four learning levels with live demonstrations.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("3. 🗺️ MAPPING TYPE INTERACTIONS")
    print("=" * 60)

    # Use the provided students for demonstrations
    student_grades = students.copy() if students else {"Alice": 95, "Bob": 87, "Charlie": 92}

    print(f"Student Grades ({student_grades}):")
    print(f"  Student names: {list(student_grades.keys())}")
    print(f"  Grades: {list(student_grades.values())}")
    print(f"  Alice's grade: {student_grades['Alice']}")
    student_grades["Diana"] = 89
    print(f"  After adding Diana: {student_grades}")

    press_enter_to_continue("Ready to explore this dictionary through layered learning?")

    try:
        # Level 1: Surface - Basic input and properties
        show_learning_level(1, "Surface Level", "Understanding what dictionaries look like and their basic properties")
        press_enter_to_continue("Ready to analyze this grade book?")

        print(f"\n🔍 LEVEL 1 ANALYSIS: {students}")
        print(f"    📊 Type: {type(students).__name__}")
        print(f"    📏 Size: {len(students)} entries")
        print(f"    📝 String representation: {str(students)}")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Practical dictionary operations
        show_learning_level(2, "Intermediate Level", "How dictionaries work in educational record keeping")
        press_enter_to_continue("See how this dictionary can be used for grade analysis?")

        if students:
            print(f"    📊 GRADE ANALYSIS:")
            print(f"      📝 Students: {list(students.keys())}")
            print(f"      📈 Grades: {list(students.values())}")

            top_student = max(students.keys(), key=lambda k: students[k])
            top_grade = students[top_student]
            print(f"      🏆 Top student: {top_student} ({top_grade})")
            print(f"      📊 Class average: {sum(students.values()) / len(students):.2f}")

            # Look up a specific student
            lookup = input("Enter a student name to look up their grade: ").strip()
            grade = students.get(lookup, "Student not found")
            print(f"      🔍 {lookup}'s grade: {grade}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - Hash table internals
        show_learning_level(3, "Deep Level", "How Python implements fast key-value lookups")
        press_enter_to_continue("Explore dictionary internals?")

        print(f"    🔬 DICTIONARY INTERNAL ANALYSIS:")
        print(f"      🆔 Memory address: {hex(id(students))} (where this dictionary lives in RAM)")
        print(f"      💾 Memory size: {sys.getsizeof(students)} bytes (space it takes up)")
        print(f"      🚫 Not hashable (mutable type)")
        print(f"        → Dictionaries can change, so they can't be used as keys")

        # Show hash values for keys
        print(f"      🔒 Key hash values:")
        for key in list(students.keys())[:3]:  # Show first 3
            print(f"        '{key}': {hash(key)} (unique number for fast lookup)")

        # Level 4: Core - Hash table implementation
        show_learning_level(4, "Core Level", "How dictionaries integrate with Python's hash table system")
        press_enter_to_continue("Explore hash table mechanics?")

        print(f"    🧬 PYTHON'S DICTIONARY SYSTEM:")
        print(f"      Let's understand how Python makes lookups lightning fast...")

        print(f"      • Dict objects: PyDictObject (hash table implementation)")
        print(f"        → Like a super-fast phone book that finds names instantly")
        print(f"      • Hashing: Keys must be hashable for fast lookups")
        print(f"        → Keys get converted to numbers for instant location")
        print(f"      • Performance: Average O(1) lookup time")
        print(f"        → Same speed whether you have 10 or 10 million entries")

        print(f"    🎯 KEY INSIGHT: Dictionaries are hash tables with Python interfaces!")
        print(f"      Your mappings become: Keys → Hashes → Table Slots → Values")

    except ValueError:
        print("❌ Please enter valid grades!")
    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_sets_layered(class_a, class_b):
    """Interactive set exploration using layered learning approach."""
    print("\n🔄 INTERACTIVE SETS - FROM SURFACE TO CORE")
    print("We'll explore unique collections through four learning levels.")

    # Show demonstrations first
    print("\n" + "=" * 60)
    print("4. 🔄 SET TYPES INTERACTIONS")
    print("=" * 60)

    # Use the provided sets for demonstrations
    unique_subjects = class_a.copy() if class_a else {"Math", "Science", "English", "History"}
    elective_subjects = class_b.copy() if class_b else {"Art", "Music", "PE", "Computer Science"}
    core_subjects = frozenset(["Math", "English"])

    print(f"Unique Subjects ({unique_subjects}):")
    unique_subjects.add("Art")
    print(f"  After add('Art'): {unique_subjects}")
    unique_subjects.remove("History")
    print(f"  After remove('History'): {unique_subjects}")
    print(f"  Union with {elective_subjects}: {unique_subjects | elective_subjects}")
    print(f"  Intersection with {elective_subjects}: {unique_subjects & elective_subjects}")

    print(f"\nCore Subjects ({core_subjects}):")
    print(f"  Union with frozenset(['Science']): {core_subjects | frozenset(['Science'])}")

    press_enter_to_continue("Ready to explore these sets through layered learning?")

    try:
        # Level 1: Surface - Basic input and properties
        show_learning_level(1, "Surface Level", "Understanding what sets look like and their basic properties")
        press_enter_to_continue("Ready to analyze these subject sets?")

        print(f"\n🔍 LEVEL 1 ANALYSIS:")
        print(f"    📚 Class A subjects: {class_a}")
        print(f"    📚 Class B subjects: {class_b}")
        print(f"    📊 Type: {type(class_a).__name__}")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Set operations
        show_learning_level(2, "Intermediate Level", "How sets work in educational subject analysis")
        press_enter_to_continue("See set operations in action?")

        print(f"    🔗 SET OPERATIONS:")
        print(f"      🔗 Union (all subjects): {class_a | class_b}")
        print(f"      ⚡ Intersection (common): {class_a & class_b}")
        print(f"      ➖ A minus B: {class_a - class_b}")
        print(f"      ➖ B minus A: {class_b - class_a}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - Set internals
        show_learning_level(3, "Deep Level", "How Python implements fast membership testing")
        press_enter_to_continue("Explore set internals?")

        print(f"    🔬 SET INTERNAL ANALYSIS:")
        print(f"      🆔 Memory address: {hex(id(class_a))} (where this set lives in RAM)")
        print(f"      💾 Memory size: {sys.getsizeof(class_a)} bytes (space it takes up)")
        print(f"      🚫 Not hashable (mutable type)")
        print(f"        → Sets can change, so they can't be used as dictionary keys")

        # Level 4: Core - Hash-based implementation
        show_learning_level(4, "Core Level", "How sets integrate with Python's hash system")
        press_enter_to_continue("Explore set implementation?")

        print(f"    🧬 PYTHON'S SET SYSTEM:")
        print(f"      Let's understand how Python keeps collections unique and fast...")

        print(f"      • Set objects: PySetObject (hash-based storage)")
        print(f"        → Like a club where each member can only join once")
        print(f"      • Uniqueness: Automatic duplicate removal")
        print(f"        → Adding the same item twice has no effect")
        print(f"      • Performance: Average O(1) membership testing")
        print(f"        → Instantly knows if an item is in the set")

        print(f"    🎯 KEY INSIGHT: Sets are hash-based collections with Python interfaces!")
        print(f"      Your collections become: Items → Hashes → Unique Storage → Fast Lookup")

    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_booleans_layered(attendance, homework, exam):
    """Interactive boolean exploration using layered learning approach."""
    print("\n✅ INTERACTIVE BOOLEANS - FROM SURFACE TO CORE")
    print("We'll explore true/false logic through four learning levels.")

    # Show brief boolean demonstrations first
    print("\n" + "=" * 60)
    print("✅ BOOLEAN BASICS DEMONSTRATION")
    print("=" * 60)

    # Use the provided booleans for demonstrations
    passed_exam = exam

    print(f"Passed Exam ({passed_exam}):")
    print(f"  AND False: {passed_exam and False}")
    print(f"  OR False: {passed_exam or False}")
    print(f"  NOT: {not passed_exam}")

    press_enter_to_continue("Ready to explore boolean logic through layered learning?")

    try:
        # Level 1: Surface - Basic input and properties
        show_learning_level(1, "Surface Level", "Understanding what booleans look like and their basic properties")
        press_enter_to_continue("Ready to analyze these conditions?")

        print(f"\n🔍 LEVEL 1 ANALYSIS:")
        print(f"    📊 Attendance: {attendance} (type: {type(attendance).__name__})")
        print(f"    📝 Homework: {homework} (type: {type(homework).__name__})")
        print(f"    📊 Exam: {exam} (type: {type(exam).__name__})")

        press_enter_to_continue("Ready to explore the intermediate level?")

        # Level 2: Intermediate - Boolean logic
        show_learning_level(2, "Intermediate Level", "How booleans work in educational decision making")
        press_enter_to_continue("See boolean logic in grading decisions?")

        can_progress = attendance and homework and exam
        needs_extra_help = not exam and (attendance or homework)
        eligible_for_bonus = attendance and homework

        print(f"    🧮 BOOLEAN LOGIC RESULTS:")
        print(f"      🎓 Can progress: {attendance} AND {homework} AND {exam} = {can_progress}")
        print(f"      🤝 Needs help: NOT {exam} AND ({attendance} OR {homework}) = {needs_extra_help}")
        print(f"      🎁 Bonus eligible: {attendance} AND {homework} = {eligible_for_bonus}")

        press_enter_to_continue("Ready to explore the deep level?")

        # Level 3: Deep - Boolean internals
        show_learning_level(3, "Deep Level", "How Python represents true and false internally")
        press_enter_to_continue("Explore how Python stores boolean values?")

        print(f"    🔬 BOOLEAN INTERNAL ANALYSIS:")
        print(f"      🆔 Memory address: {hex(id(True))} (where True is stored in computer memory)")
        print(f"      🆔 False address: {hex(id(False))} (where False is stored in computer memory)")
        print(f"      💾 True size: {sys.getsizeof(True)} bytes (memory space used)")
        print(f"      💾 False size: {sys.getsizeof(False)} bytes (memory space used)")
        print(f"      🔒 True hash: {hash(True)} (unique identifier for True)")
        print(f"      🔒 False hash: {hash(False)} (unique identifier for False)")

        press_enter_to_continue("Ready to explore the core level?")

        # Level 4: Core - Boolean as integers
        show_learning_level(4, "Core Level", "How booleans integrate with Python's type system")
        press_enter_to_continue("Explore the surprising truth about booleans?")

        print(f"    🧬 PYTHON'S BOOLEAN SYSTEM:")
        print(f"      • Boolean objects: Subclass of int (True = 1, False = 0)")
        print(f"        → This means booleans ARE numbers in disguise!")
        print(f"      • Singleton objects: Only one True and one False exist")
        print(f"        → Every True you see is the same object in memory")
        print(f"      • Arithmetic: Booleans work in math (True + True = 2)")

        print(f"      📊 Proof: True + True = {True + True}")
        print(f"      📊 Proof: False * 3 = {False * 3}")

        print(f"    🎯 KEY INSIGHT: Booleans are integers with logical names!")
        print(f"      Your logic becomes: Conditions → True/False → 1/0 → Arithmetic")

    except Exception as e:
        print(f"❌ Error: {e}")

interactive_menu()

interactive_menu()

