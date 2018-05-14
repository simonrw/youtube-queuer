#[macro_use]
extern crate structopt;
extern crate futures;
extern crate hyper;
extern crate youtube_queuer as yt;

use futures::future::Future;
use hyper::header::ContentLength;
use hyper::server::{Http, Request, Response, Service};
use structopt::StructOpt;

#[derive(StructOpt, Debug)]
struct Opt {
    #[structopt(short = "p", long = "port")]
    port: Option<u32>,
    #[structopt(short = "H", long = "host")]
    host: Option<String>,
}

struct Ytld;

const PHRASE: &'static str = "Hello world";

impl Service for Ytld {
    type Request = Request;
    type Response = Response;
    type Error = hyper::Error;

    type Future = Box<Future<Item = Self::Response, Error = Self::Error>>;

    fn call(&self, _req: Request) -> Self::Future {
        println!("Got request");
        Box::new(futures::future::ok(
            Response::new()
                .with_header(ContentLength(PHRASE.len() as _))
                .with_body(PHRASE),
        ))
    }
}

fn main() {
    let opt: Opt = Opt::from_args();
    let port = opt.port.unwrap_or(yt::DEFAULT_PORT);
    let host = opt.host.unwrap_or(yt::DEFAULT_HOST.to_string());

    let addr = format!("{}:{}", host, port).parse().unwrap();
    let server = Http::new().bind(&addr, || Ok(Ytld)).unwrap();
    server.run().unwrap();
}
