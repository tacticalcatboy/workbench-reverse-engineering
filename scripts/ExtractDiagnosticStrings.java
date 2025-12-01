//Extracts diagnostic-related strings from the analyzed binary
//@category Analysis
//@keybinding
//@menupath
//@toolbar

import ghidra.app.script.GhidraScript;
import ghidra.program.model.data.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.*;
import java.io.*;
import java.util.*;

public class ExtractDiagnosticStrings extends GhidraScript {

    // Keywords that indicate diagnostic messages
    private static final String[] DIAGNOSTIC_KEYWORDS = {
        "is not used",
        "not used",
        "obsolete",
        "deprecated",
        "conflict",
        "can be const",
        "could be const",
        "No need to use",
        "warning",
        "Warning",
        "error",
        "Error",
        "hint",
        "Hint",
        "Variable",
        "overwrites",
        "ResourceName",
        "picker",
        "Cast",
        "up-cast",
        "upcast",
        "script default value",
        "Possible variable"
    };

    @Override
    public void run() throws Exception {
        File outputFile = new File(getSourceFile().getParentFile(), "extracted_strings.txt");
        File diagnosticFile = new File(getSourceFile().getParentFile(), "diagnostic_strings.txt");

        PrintWriter allWriter = new PrintWriter(new FileWriter(outputFile));
        PrintWriter diagWriter = new PrintWriter(new FileWriter(diagnosticFile));

        println("Extracting strings from: " + currentProgram.getName());
        println("Output files:");
        println("  All strings: " + outputFile.getAbsolutePath());
        println("  Diagnostic strings: " + diagnosticFile.getAbsolutePath());

        DataIterator dataIterator = currentProgram.getListing().getDefinedData(true);
        Set<String> diagnosticStrings = new TreeSet<>();
        int totalStrings = 0;

        while (dataIterator.hasNext() && !monitor.isCancelled()) {
            Data data = dataIterator.next();
            DataType dt = data.getDataType();

            // Check for string types
            if (dt instanceof StringDataType ||
                dt instanceof TerminatedStringDataType ||
                dt instanceof UnicodeDataType ||
                dt instanceof Unicode32DataType ||
                dt.getName().toLowerCase().contains("string")) {

                Object value = data.getValue();
                if (value != null) {
                    String str = value.toString();
                    if (str.length() >= 8 && str.length() <= 500) {
                        totalStrings++;
                        allWriter.println(str);

                        // Check for diagnostic keywords
                        for (String keyword : DIAGNOSTIC_KEYWORDS) {
                            if (str.contains(keyword)) {
                                diagnosticStrings.add(str);
                                break;
                            }
                        }
                    }
                }
            }
        }

        // Write diagnostic strings
        diagWriter.println("=== DIAGNOSTIC-RELATED STRINGS FROM WORKBENCH ===");
        diagWriter.println("Total strings scanned: " + totalStrings);
        diagWriter.println("Diagnostic strings found: " + diagnosticStrings.size());
        diagWriter.println("================================================\n");

        for (String s : diagnosticStrings) {
            diagWriter.println(s);
        }

        allWriter.close();
        diagWriter.close();

        println("\nExtraction complete!");
        println("Total strings: " + totalStrings);
        println("Diagnostic strings: " + diagnosticStrings.size());

        // Also print diagnostic strings to console
        println("\n=== DIAGNOSTIC STRINGS ===\n");
        for (String s : diagnosticStrings) {
            println("  " + s);
        }
    }
}
