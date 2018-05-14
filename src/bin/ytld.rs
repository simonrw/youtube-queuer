#[macro_use]
extern crate structopt;
extern crate youtube_queuer as yt;

use structopt::StructOpt;

#[derive(StructOpt, Debug)]
struct Opt {
    #[structopt(short = "p", long = "port")]
    port: Option<u32>,
    #[structopt(short = "H", long = "host")]
    host: Option<String>,
}

fn main() {
    let opt: Opt = Opt::from_args();
    let port = opt.port.unwrap_or(yt::DEFAULT_PORT);
    let host = opt.host.unwrap_or(yt::DEFAULT_HOST.to_string());
}
