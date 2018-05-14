#[macro_use]
extern crate structopt;
extern crate futures;
extern crate hyper;
extern crate youtube_queuer as yt;

use futures::future::Future;
use hyper::server::{Http, Request, Response, Service};
use hyper::{Method, StatusCode};
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

    fn call(&self, req: Request) -> Self::Future {
        let mut response = Response::new();

        match (req.method(), req.path()) {
            (Method::Get, "/") => {
                response.set_body(PHRASE);
            }
            _ => {
                response.set_status(StatusCode::NotFound);
            }
        }

        Box::new(futures::future::ok(response))
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
