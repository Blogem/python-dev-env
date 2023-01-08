# PySpark local development
When using PySpark it is necessary to connect to a Spark runtime. A single node runtime is automatically installed when installing PySpark (e.g. through poetry or pip), which can be used for local development. To use PySpark, Java is required. On macOS this can be installed using several options.

After installation PySpark should work from the terminal (open a new one to make sure the new profile is sourced). VS Code might require a full reboot to find Java.

## Option 1 (20220811, MacBook M1)
```
brew install openjdk@11
echo 'export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc  # per brew install instructions
```

## Option 2 (20220707)
```
brew tap adoptopenjdk/openjdk
brew install adoptopenjdk13 --cask
```

