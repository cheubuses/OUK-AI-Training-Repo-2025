

walker first {
    with entry {
        report("Hello Jaseci");      
    }
}

walker second {
    with entry {
        report("Hello my world");
    }
}

walker second {
    with entry {
        report("Jaseci is very interesting indeed");
    }
}

walker thirs {
    with entry {
        def squarer(x:int) -> int {
            return x ** 2 ;
        }
        print(squarer(5));
    }
}
