
function [bestX, bestScore, exitflag, output] = run_face_ga(projectRoot)
%RUN_FACE_GA Run MATLAB Genetic Algorithm using Python fitness.
%
% projectRoot is the EvolveMySketch project directory.
% Python evaluates every candidate through evaluate_candidate().

    arguments
        projectRoot (1,1) string
    end

    % Add the Python source directory to Python's module search path.
    pythonSrc = fullfile(projectRoot, "src");

    if ~isfolder(pythonSrc)
        error("Python source directory not found: %s", pythonSrc);
    end

    py.sys.path.insert(int32(0), char(pythonSrc));

    % Import the Python objective adapter.
    objectiveModule = py.importlib.import_module( ...
        "EvolveMySketch.optimization_interface");

    % MATLAB GA decision-variable count.
    nvars = 10;

    % Initial design bounds.
    % These are starting assumptions for the normalized face canvas.
    lb = [
        0.35, ... % face_width
        0.45, ... % face_height
        0.12, ... % eye_spacing
        0.25, ... % eye_y
        0.025, ... % eye_size
        0.20, ... % brow_y
        0.08, ... % nose_length
        0.025, ... % nose_width
        0.12, ... % mouth_width
        0.55  ... % mouth_y
    ];

    ub = [
        0.65, ... % face_width
        0.75, ... % face_height
        0.30, ... % eye_spacing
        0.50, ... % eye_y
        0.08, ... % eye_size
        0.50, ... % brow_y
        0.18, ... % nose_length
        0.08, ... % nose_width
        0.25, ... % mouth_width
        0.75  ... % mouth_y
    ];

    % MATLAB calls the Python adapter for each candidate.
    objective = @(x) evaluatePythonFitness(objectiveModule, x);

    options = optimoptions("ga", ...
        "Display", "iter", ...
        "PopulationSize", 50, ...
        "MaxGenerations", 100);

    [bestX, bestScore, exitflag, output] = ga( ...
        objective, nvars, ...
        [], [], [], [], ...
        lb, ub, [], options);
end


function score = evaluatePythonFitness(objectiveModule, x)
% Convert MATLAB candidate vector to a NumPy array and call Python.

    pythonX = py.numpy.array(x);
    pythonScore = objectiveModule.evaluate_candidate(pythonX);

    score = double(pythonScore);
end
