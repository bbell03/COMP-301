
void main() {
    for (test in ListOfTestCases) {
        Expr expanded = desugar(test.input);
        String as_c_prog = expanded.as_c();
        print_to_file(as_c_prog, "x.c");
        compile("x.c");
        String output = run_and_get_output("x.bin");
    
        if(output != test.output) {
            report_an_error(); 
        }
    }