final_test = """
int a = 10;
a = 20;
string b = "20";
char abs = "c";

int count = 0;
void something() {
    WriteLine("Hello");
}

WriteLine("Test calling function that prints Hello");
something();
int c = 10;
WriteLine("Test: 10 + 10:");
WriteLine(a + c);
int[] arr = { 1, 2, 3, 2, 3, 4 };
WriteLine("Printing arr = [1, 2, 3, 2, 3, 4]:");
WriteLine(arr);
WriteLine("Printing arr[1]:");
WriteLine(arr[1]);
WriteLine("Changing arr[1] to 20:");
arr[1] = 20;
WriteLine(arr[1]);

bool testBool = true;
bool testBool2 = false;

if (testBool && testBool2 || false) {
    WriteLine("if went to true");
} else {
    WriteLine("if went to false");
}

int count1 = 2;
while (count < 5) {
    count += 1;
    count1 *= 2;
}
WriteLine(count);
WriteLine(count1);

class Some {
    int sum(int a, int b) {
        return a + b;
    }
}

class Something: Some {
    void test() {
        WriteLine("Calling parent class method:");
        int sumResult = base.sum(10, 5);
        WriteLine(sumResult);
    }
}
Something().test();

class EmptyClass {}
"""
sharpCode = """
int a = 10;
a = 20;
string b = "20";
char abs = "c";

int count = 0;
void something() {
    WriteLine("Hello");
}

WriteLine("Test calling function that prints Hello");
something();
int c = 10;
WriteLine("Test: 10 + 10:");
WriteLine(a + c);
int[] arr = { 1, 2, 3, 2, 3, 4 };
WriteLine("Printing arr = [1, 2, 3, 2, 3, 4]:");
WriteLine(arr);
WriteLine("Printing arr[1]:");
WriteLine(arr[1]);
WriteLine("Changing arr[1] to 20:");
arr[1] = 20;
WriteLine(arr[1]);

bool testBool = true;
bool testBool2 = false;

if (testBool && testBool2 || false) {
    WriteLine("if went to true");
} else {
    WriteLine("if went to false");
}

int count1 = 2;
while (count < 5) {
    count += 1;
    count1 *= 2;
}
WriteLine(count);
WriteLine(count1);
"""

from Runtime.Language_.callbacks import report_error, runtime_error, scanner_error, init_language
from Runtime.Language_.language import Language

#
# def main_scanner_error(line, message):
#     print(f"[line {line}] ScannerError: {message}")
#
#
# # Use the new set_scanner_error_handler function
# Language.set_scanner_error_handler(main_scanner_error)

sharpCode1 = """
int a = 10;

char abs = "c";
string str = "Nigger";

int count = 0;
int something() {
    WriteLine("Hello");
}
"""
Language.run(final_test)

# try Lox.runPrompt()
# try Lox.runFile(path: "testCode.txt")
