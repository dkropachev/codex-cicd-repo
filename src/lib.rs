pub fn normalize_name(input: &str) -> String {
    input.trim().to_lowercase()
}

#[cfg(test)]
mod tests {
    use super::normalize_name;

    #[test]
    fn normalizes_name() {
        assert_eq!(normalize_name(" Codex "), "codex");
    }
}
