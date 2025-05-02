# notes

How to write beautiful Golang CLI [yt-vid](https://www.youtube.com/watch?v=SSRIn5DAmyw)

## Install Cobra

### Be on the path

Make sure you have the correct path in your `.zshrc` or your shell file

```sh
cd ~             # if not in the root dir
nvim .zshrc      # edit the file
```

Add this lines on your shell source file:

```sh
########################### Go ##############################
# add the default Go binary directory to your `PATH`
export PATH="$PATH:$(go env GOPATH)/bin"

# `GOBIN` controls where Go places installed binaries.
# USAGE: $ export $PATH=$PATH:$GOBIN
export GOBIN=~/go/bin/
```

### After save the `.zshrc`

```sh
source ~/.zshrc # Re source the file in your shell
exec zsh   # Rerun the shell
```

### Download and install Cobra

```sh
go install github.com/spf13/cobra-cli@latest
`cobra-cli`        # check if it is installed
```

### Initialize in your project

Init in the folder where you want it to be created

```sh
cobra-cli init [folder_name]
```

It will create a folder with the `folder_name` with this layout:

-- `folder_name`
    |
    |- cmd
    |   |- root.go
    |
    |- go.mod
    |- go.sum
    |- LICENSE
    |- main.go

### Check if the code can run:

```sh
go run main.go
```

after run it, It will output:

"""
A longer description that spans multiple lines and likely contains
examples and usage of using your application. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.
"""

## How it works

On `main.go` the `cmd.Execute()` will call on the root command( `root.go`), all the syntax occurs on the root.

You will have object to `struct` for any command that you create it will populate with these parameters:

```go
var rootCmd = &cobra.Command{
	Use:   "learn-cobra",
	Short: "A brief description of your application",
	Long: `A longer description that spans multiple lines and likely contains
examples and usage of using your application. For example:.`,
}
```

And then it will on the `root.go` command from the `main.go`

## Add ping and notes

To create those go files

```sh
cobra-cli add net
cobra-cli add ping
