function [base_frame, tool_frame, tf_array] = parser(tf_array_path, base_frame_path, tool_frame_path, flage_frame_path)
    pyenv('Version', '/usr/bin/python3');

    if count(py.sys.path, './') == 0
        insert(py.sys.path, int32(0), './');
    end

    result = py.parser.parse( ...
        tf_array_path, ...
        base_frame_path, ...
        tool_frame_path, ...
        flage_frame_path);

    base_frame = result{1};
    tool_frame = result{2};
    tf_array = result{3};
end
