package main

import(
    "net/http"
    "os/exec"
    "runtime"
    "fmt"
)

func main() {
    
    var (
        dir string
        port string
    )
    dir = "./web/"
    port = "8000"
    // fmt.Printf("Please input which directory\nwhat you want to share, start with \"/\":\n")
    // fmt.Scanf("%s",&dir)
    h := http.FileServer(http.Dir(dir))
    // fmt.Scanf("%s",&port)
    fmt.Printf("ScratchX 伺服器執行中.... \n")
    open("http://127.0.0.1:8000")
    http.ListenAndServe(":"+port, h)
}

// open opens the specified URL in the default browser of the user.
func open(url string) error {
    var cmd string
    var args []string

    switch runtime.GOOS {
    case "windows":
        cmd = "cmd" 
        args = []string{"/c", "explorer"}
    case "darwin":
        cmd = "open"
    default: // "linux", "freebsd", "openbsd", "netbsd"
        cmd = "xdg-open"
    }
    args = append(args, url)
    return exec.Command(cmd, args...).Start()
}