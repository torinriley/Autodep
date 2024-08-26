require 'find'

def scan_for_dependencies(directory = '.')
  dependencies = []

  Find.find(directory) do |path|
    if File.extname(path) == '.rb'
      File.readlines(path).each do |line|
        match = line.match(/^\s*require\s+['"](.+?)['"]/)
        dependencies << match[1] if match && !match[1].start_with?('.')
      end
    end
  end

  dependencies.uniq
end

def generate_gemfile(dependencies, output_path = 'Gemfile')
  gemfile_content = <<~HEREDOC
    source "https://rubygems.org"

    gemspec
  HEREDOC

  dependencies.each do |dep|
    gemfile_content << "gem '#{dep}'\n"
  end

  File.write(output_path, gemfile_content)
  puts "Gemfile generated successfully at #{output_path}."
end

if __FILE__ == $0
  directory = ARGV.find { |arg| arg.start_with?('--dir=') }&.split('=')&.last || '.'
  output_path = ARGV.find { |arg| arg.start_with?('--output=') }&.split('=')&.last || 'Gemfile'

  dependencies = scan_for_dependencies(directory)
  generate_gemfile(dependencies, output_path)
end
