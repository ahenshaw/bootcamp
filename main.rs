use structopt::StructOpt;
use std::time::Instant;

// handle command-line options
#[derive(StructOpt, Debug)]
#[structopt(name = "basic")]
struct Opt {
    #[structopt(short, long, default_value = "3000")]
    n: usize,
}


fn main() {
    let opt = Opt::from_args();
    let n = opt.n;
    let mut total = 0;
    println!("using n={}", n);
    // build the matrix
    let start = Instant::now();
    for _ in 0..n {
        for j in 0..n {
            total += if j >= n/2 {1} else {-1};
        }
    }
    
    println!("elapsed time: {:?}", Instant::now() - start);
    println!("result: {}", total);
}
