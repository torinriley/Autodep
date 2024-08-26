import os
import re

def scan_for_python_dependencies(directory):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        match = re.match(r'^\s*(import|from)\s+(\S+)', line)
                        if match:
                            dependencies.add(match.group(2).split('.')[0])
    return dependencies

def scan_for_javascript_dependencies(directory):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.js', '.ts')):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        match = re.search(r'require\([\'"](.+?)[\'"]\)|import\s+[^\'"]*[\'"](.+?)[\'"]', line)
                        dep = match.group(1) if match and match.group(1) else match.group(2)
                        if dep and not dep.startswith('.'):
                            dependencies.add(dep)
                              return dependencies

def scan_for_ruby_dependencies(directory):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rb'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        match = re.match(r'^\s*require\s*[\'"](.+?)[\'"]', line)
                        if match and not match.group(1).startswith('.'):
                            dependencies.add(match.group(1))
                              return dependencies

def scan_for_php_dependencies(directory):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.php'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        match = re.match(r'^\s*(use|require|include)\s*[\'"](.+?)[\'"]', line)
                        if match and not match.group(2).startswith('.'):
                            dependencies.add(match.group(2).split('.')[0])
                              return dependencies

def scan_for_go_dependencies(directory):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.go'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        match = re.match(r'^\s*import\s*[\'"](.+?)[\'"]', line)
                        if match and not match.group(1).startswith('.'):
                            dependencies.add(match.group(1))
                              return dependencies

def scan_for_java_dependencies(directory):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        match = re.match(r'^\s*import\s+([\w\.]+)', line)
                        if match and not match.group(1).startswith('java'):
                            dependencies.add(match.group(1).split('.')[0])
                              return dependencies

def generate_requirements_txt(dependencies):
    with open('requirements.txt', 'w') as f:
        for dep in dependencies:
            f.write(f"{dep}\n")
    print("requirements.txt generated successfully.")

def generate_package_json(dependencies):
    package_json = {
        "dependencies": {dep: "*" for dep in dependencies}
    }
    with open('package.json', 'w') as f:
        f.write(json.dumps(package_json, indent=2))
    print("package.json generated successfully.")

def generate_gemfile(dependencies):
    with open('Gemfile', 'w') as f:
        f.write("source 'https://rubygems.org'\n\n")
        for dep in dependencies:
            f.write(f"gem '{dep}'\n")
    print("Gemfile generated successfully.")

def generate_composer_json(dependencies):
    composer_json = {
        "require": {dep: "*" for dep in dependencies}
    }
    with open('composer.json', 'w') as f:
        f.write(json.dumps(composer_json, indent=2))
    print("composer.json generated successfully.")

def generate_go_mod(dependencies):
    with open('go.mod', 'w') as f:
        f.write("module your_module_name\n\n")
        f.write("go 1.16\n\n")
        for dep in dependencies:
            f.write(f"require {dep} latest\n")
    print("go.mod generated successfully.")

def generate_pom_xml(dependencies):
    with open('pom.xml', 'w') as f:
        f.write("<project>\n")
        f.write("  <modelVersion>4.0.0</modelVersion>\n")
        f.write("  <dependencies>\n")
        for dep in dependencies:
            f.write(f"    <dependency>\n")
            f.write(f"      <groupId>{dep}</groupId>\n")
            f.write(f"      <artifactId>{dep}</artifactId>\n")
            f.write(f"      <version>latest</version>\n")
            f.write(f"    </dependency>\n")
        f.write("  </dependencies>\n")
        f.write("</project>\n")
    print("pom.xml generated successfully.")

def main():
    directory = '.'  
    python_deps = scan_for_python_dependencies(directory)
    javascript_deps = scan_for_javascript_dependencies(directory)
    ruby_deps = scan_for_ruby_dependencies(directory)
    php_deps = scan_for_php_dependencies(directory)
    go_deps = scan_for_go_dependencies(directory)
    java_deps = scan_for_java_dependencies(directory)

    if python_deps:
        generate_requirements_txt(python_deps)

    if javascript_deps:
        generate_package_json(javascript_deps)

    if ruby_deps:
        generate_gemfile(ruby_deps)

    if php_deps:
        generate_composer_json(php_deps)

    if go_deps:
        generate_go_mod(go_deps)

    if java_deps:
        generate_pom_xml(java_deps)

if __name__ == "__main__":
    main()
